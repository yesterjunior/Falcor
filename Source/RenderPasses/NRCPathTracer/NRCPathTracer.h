#pragma once
#include "Falcor.h"
#include "RenderPasses/Shared/PathTracer/PathTracer.h"
#include "NRC.h"
#include "Network.h"
#include "Utils/SampleGenerators/HaltonSamplePattern.h"
#include "Debug/NRCPixelStats.h"

using namespace Falcor;


/** Forward path tracer using a NRC.

    The path tracer has a loop over the path vertices in the raygen shader.
    The kernel terminates when all paths have terminated.

    This pass implements a forward path tracer with next-event estimation,
    Russian roulette, and multiple importance sampling (MIS) with sampling
    of BRDFs and light sources.
*/
class NRCPathTracer : public PathTracer
{
public:
    using SharedPtr = std::shared_ptr<NRCPathTracer>;

    //static SharedPtr create(RenderContext* pRenderContext, const Dictionary& dict);
    static ref<NRCPathTracer> create(ref<Device> pDevice, const Properties& props);

    //virtual std::string getDesc() override { return sDesc; }
    
    //virtual void setScene(RenderContext* pRenderContext, const Scene::SharedPtr& pScene) override;
    virtual void setScene(RenderContext* pRenderContext, const ref<Scene>& pScene) override;
    virtual void renderUI(Gui::Widgets& widget) override;
    virtual void execute(RenderContext* pRenderContext, const RenderData& renderData) override;
    virtual RenderPassReflection reflect(const CompileData& compileData) override;

    static const char* sDesc;

private:
    //NRCPathTracer(const Dictionary& dict);
    NRCPathTracer(ref<Device> pDevice, const Properties& props);

    //~NRCPathTracer();

    // these 2 functions are called within execute()
    bool beginFrame(RenderContext* pRenderContext, const RenderData& renderData);
    void endFrame(RenderContext* pRenderContext, const RenderData& renderData);



    //void recreateVars() override { mTracer.pVars = nullptr; }
    void prepareVars();
    void setTracerData(const RenderData& renderData);
    void setNRCData(const RenderData& renderData);

    // Ray tracing program.
    struct
    {
        ref<RtProgram> pProgram;
        ref<NRCPixelStats> pNRCPixelStats;
        ref<RtBindingTable> pBindingTable;
        ref<RtProgramVars> pVars;
        ref<ParameterBlock> pParameterBlock; ///< ParameterBlock for all data.
    } mTracer;

    // Neural radiance cache parameters and data fields
    struct {
        ref<NRC::NRCInterface> pNRC = nullptr;
        ref<NRC::NRCNetwork> pNetwork = nullptr;

        bool enableNRC = true;
        bool visualizeNRC = false;
        uint32_t visualizeMode = 1;
        float prob_rr_suffix_absorption = 0.2f;
        float footprint_thres_inference = 2.5f;
        float foorprint_thres_suffix = 20.f;

        int max_training_bounces = 5;               // max path segments for training suffix
        int max_training_rr_bounces = 10;
        int max_inference_bounces = 5;

        ref<Buffer> pTrainingRadianceQuery = nullptr;
        ref<Buffer> pTrainingRadianceSample = nullptr;
        ref<Buffer> pInferenceRadianceQuery = nullptr;
        ref<Buffer> pInferenceRadiancePixel = nullptr;
        ref<Buffer> pSharedCounterBuffer = nullptr;
        ref<Texture> pScreenQueryFactor = nullptr;
        ref<Texture> pScreenQueryBias = nullptr;
        ref<Texture> pScreenQueryReflectance = nullptr;
        ref<Texture> pScreenResult = nullptr;

    } mNRC;

    bool mNRCOptionChanged = true;
    ref<ComputePass> mCompositePass;
    ref<HaltonSamplePattern> mHaltonSampler;
};
