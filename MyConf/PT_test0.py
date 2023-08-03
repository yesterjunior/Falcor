# Graphs
from pathlib import WindowsPath, PosixPath
from falcor import *

def render_graph_DefaultRenderGraph():
    g = RenderGraph('DefaultRenderGraph')
    g.create_pass('GBufferRT', 'GBufferRT', {'outputSize': 'Default', 'samplePattern': 'Center', 'sampleCount': 16, 'useAlphaTest': True, 'adjustShadingNormals': True, 'forceCullMode': False, 'cull': 'Back', 'texLOD': 'Mip0', 'useTraceRayInline': False, 'useDOF': False})
    g.create_pass('AccumulatePass', 'AccumulatePass', {'enabled': True, 'outputSize': 'Default', 'autoReset': True, 'precisionMode': 'Single', 'maxFrameCount': 0, 'overflowMode': 'Stop'})
    g.create_pass('ToneMapper', 'ToneMapper', {'outputSize': 'Default', 'useSceneMetadata': True, 'exposureCompensation': 0.0, 'autoExposure': False, 'filmSpeed': 100.0, 'whiteBalance': False, 'whitePoint': 6500.0, 'operator': 'Aces', 'clamp': True, 'whiteMaxLuminance': 1.0, 'whiteScale': 11.199999809265137, 'fNumber': 1.0, 'shutter': 1.0, 'exposureMode': 'AperturePriority'})
    g.create_pass('SDFEditor', 'SDFEditor', {})
    g.create_pass('PathTracer', 'PathTracer', {'samplesPerPixel': 1, 'maxSurfaceBounces': 10, 'maxDiffuseBounces': 3, 'maxSpecularBounces': 3, 'maxTransmissionBounces': 10, 'sampleGenerator': 0, 'useBSDFSampling': True, 'useRussianRoulette': False, 'useNEE': True, 'useMIS': True, 'misHeuristic': 'Balance', 'misPowerExponent': 2.0, 'emissiveSampler': 'LightBVH', 'lightBVHOptions': {'buildOptions': {'splitHeuristicSelection': 'BinnedSAOH', 'maxTriangleCountPerLeaf': 10, 'binCount': 16, 'volumeEpsilon': 0.0010000000474974513, 'splitAlongLargest': False, 'useVolumeOverSA': False, 'useLeafCreationCost': True, 'createLeavesASAP': True, 'allowRefitting': True, 'usePreintegration': True, 'useLightingCones': True}, 'useBoundingCone': True, 'useLightingCone': True, 'disableNodeFlux': False, 'useUniformTriangleSampling': True, 'solidAngleBoundMethod': 'Sphere'}, 'useRTXDI': False, 'RTXDIOptions': {'mode': 'SpatiotemporalResampling', 'presampledTileCount': 128, 'presampledTileSize': 1024, 'storeCompactLightInfo': True, 'localLightCandidateCount': 24, 'infiniteLightCandidateCount': 8, 'envLightCandidateCount': 8, 'brdfCandidateCount': 1, 'brdfCutoff': 0.0, 'testCandidateVisibility': True, 'biasCorrection': 'Basic', 'depthThreshold': 0.10000000149011612, 'normalThreshold': 0.5, 'samplingRadius': 30.0, 'spatialSampleCount': 1, 'spatialIterations': 5, 'maxHistoryLength': 20, 'boilingFilterStrength': 0.0, 'rayEpsilon': 0.0010000000474974513, 'useEmissiveTextures': False, 'enableVisibilityShortcut': False, 'enablePermutationSampling': False}, 'useAlphaTest': True, 'adjustShadingNormals': False, 'maxNestedMaterials': 2, 'useLightsInDielectricVolumes': False, 'disableCaustics': False, 'specularRoughnessThreshold': 0.25, 'primaryLodMode': 'Mip0', 'lodBias': 0.0, 'useNRDDemodulation': True, 'outputSize': 'Default', 'colorFormat': 'LogLuvHDR'})
    g.add_edge('GBufferRT.vbuffer', 'PathTracer.vbuffer')
    g.add_edge('GBufferRT.viewW', 'PathTracer.viewW')
    g.add_edge('GBufferRT.mvecW', 'PathTracer.mvec')
    g.add_edge('GBufferRT.vbuffer', 'SDFEditor.vbuffer')
    g.add_edge('GBufferRT.linearZ', 'SDFEditor.linearZ')
    g.add_edge('PathTracer.color', 'AccumulatePass.input')
    g.add_edge('AccumulatePass.output', 'ToneMapper.src')
    g.add_edge('ToneMapper.dst', 'SDFEditor.inputColor')
    g.mark_output('SDFEditor.output')
    return g
m.addGraph(render_graph_DefaultRenderGraph())
from pathlib import WindowsPath, PosixPath
from falcor import *

def render_graph_PathTracerNRD():
    g = RenderGraph('PathTracerNRD')
    g.create_pass('GBufferRT', 'GBufferRT', {'outputSize': 'Default', 'samplePattern': 'Halton', 'sampleCount': 32, 'useAlphaTest': True, 'adjustShadingNormals': True, 'forceCullMode': False, 'cull': 'Back', 'texLOD': 'Mip0', 'useTraceRayInline': False, 'useDOF': True})
    g.create_pass('PathTracer', 'PathTracer', {'samplesPerPixel': 1, 'maxSurfaceBounces': 10, 'maxDiffuseBounces': 10, 'maxSpecularBounces': 10, 'maxTransmissionBounces': 10, 'sampleGenerator': 0, 'useBSDFSampling': True, 'useRussianRoulette': True, 'useNEE': True, 'useMIS': True, 'misHeuristic': 'Balance', 'misPowerExponent': 2.0, 'emissiveSampler': 'LightBVH', 'lightBVHOptions': {'buildOptions': {'splitHeuristicSelection': 'BinnedSAOH', 'maxTriangleCountPerLeaf': 10, 'binCount': 16, 'volumeEpsilon': 0.0010000000474974513, 'splitAlongLargest': False, 'useVolumeOverSA': False, 'useLeafCreationCost': True, 'createLeavesASAP': True, 'allowRefitting': True, 'usePreintegration': True, 'useLightingCones': True}, 'useBoundingCone': True, 'useLightingCone': True, 'disableNodeFlux': False, 'useUniformTriangleSampling': True, 'solidAngleBoundMethod': 'Sphere'}, 'useRTXDI': False, 'RTXDIOptions': {'mode': 'SpatiotemporalResampling', 'presampledTileCount': 128, 'presampledTileSize': 1024, 'storeCompactLightInfo': True, 'localLightCandidateCount': 24, 'infiniteLightCandidateCount': 8, 'envLightCandidateCount': 8, 'brdfCandidateCount': 1, 'brdfCutoff': 0.0, 'testCandidateVisibility': True, 'biasCorrection': 'Basic', 'depthThreshold': 0.10000000149011612, 'normalThreshold': 0.5, 'samplingRadius': 30.0, 'spatialSampleCount': 1, 'spatialIterations': 5, 'maxHistoryLength': 20, 'boilingFilterStrength': 0.0, 'rayEpsilon': 0.0010000000474974513, 'useEmissiveTextures': False, 'enableVisibilityShortcut': False, 'enablePermutationSampling': False}, 'useAlphaTest': True, 'adjustShadingNormals': False, 'maxNestedMaterials': 2, 'useLightsInDielectricVolumes': False, 'disableCaustics': False, 'specularRoughnessThreshold': 0.25, 'primaryLodMode': 'Mip0', 'lodBias': 0.0, 'useNRDDemodulation': True, 'outputSize': 'Default', 'colorFormat': 'LogLuvHDR'})
    g.create_pass('AccumulatePass', 'AccumulatePass', {'enabled': True, 'outputSize': 'Default', 'autoReset': True, 'precisionMode': 'Single', 'maxFrameCount': 0, 'overflowMode': 'Stop'})
    g.create_pass('ToneMapperReference', 'ToneMapper', {'outputSize': 'Default', 'useSceneMetadata': True, 'exposureCompensation': 0.0, 'autoExposure': False, 'filmSpeed': 100.0, 'whiteBalance': False, 'whitePoint': 6500.0, 'operator': 'Aces', 'clamp': True, 'whiteMaxLuminance': 1.0, 'whiteScale': 11.199999809265137, 'fNumber': 1.0, 'shutter': 1.0, 'exposureMode': 'AperturePriority'})
    g.create_pass('NRDDiffuseSpecular', 'NRD', {'enabled': True, 'method': 'RelaxDiffuseSpecular', 'outputSize': 'Default', 'worldSpaceMotion': True, 'disocclusionThreshold': 2.0, 'maxIntensity': 250.0, 'diffusePrepassBlurRadius': 16.0, 'specularPrepassBlurRadius': 16.0, 'diffuseMaxAccumulatedFrameNum': 31, 'specularMaxAccumulatedFrameNum': 31, 'diffuseMaxFastAccumulatedFrameNum': 2, 'specularMaxFastAccumulatedFrameNum': 2, 'diffusePhiLuminance': 2.0, 'specularPhiLuminance': 1.0, 'diffuseLobeAngleFraction': 0.800000011920929, 'specularLobeAngleFraction': 0.8999999761581421, 'roughnessFraction': 0.5, 'diffuseHistoryRejectionNormalThreshold': 0.0, 'specularVarianceBoost': 1.0, 'specularLobeAngleSlack': 10.0, 'disocclusionFixEdgeStoppingNormalPower': 8.0, 'disocclusionFixMaxRadius': 32.0, 'disocclusionFixNumFramesToFix': 4, 'historyClampingColorBoxSigmaScale': 2.0, 'spatialVarianceEstimationHistoryThreshold': 4, 'atrousIterationNum': 6, 'minLuminanceWeight': 0.0, 'depthThreshold': 0.019999999552965164, 'luminanceEdgeStoppingRelaxation': 0.5, 'normalEdgeStoppingRelaxation': 0.30000001192092896, 'roughnessEdgeStoppingRelaxation': 0.30000001192092896, 'enableAntiFirefly': False, 'enableReprojectionTestSkippingWithoutMotion': False, 'enableSpecularVirtualHistoryClamping': False, 'enableRoughnessEdgeStopping': True, 'enableMaterialTestForDiffuse': False, 'enableMaterialTestForSpecular': False})
    g.create_pass('NRDDeltaReflection', 'NRD', {'enabled': True, 'method': 'RelaxDiffuse', 'outputSize': 'Default', 'worldSpaceMotion': False, 'disocclusionThreshold': 2.0, 'maxIntensity': 250.0, 'diffusePrepassBlurRadius': 16.0, 'diffuseMaxAccumulatedFrameNum': 31, 'diffuseMaxFastAccumulatedFrameNum': 2, 'diffusePhiLuminance': 2.0, 'diffuseLobeAngleFraction': 0.800000011920929, 'diffuseHistoryRejectionNormalThreshold': 0.0, 'disocclusionFixEdgeStoppingNormalPower': 8.0, 'disocclusionFixMaxRadius': 32.0, 'disocclusionFixNumFramesToFix': 4, 'historyClampingColorBoxSigmaScale': 2.0, 'spatialVarianceEstimationHistoryThreshold': 1, 'atrousIterationNum': 6, 'minLuminanceWeight': 0.0, 'depthThreshold': 0.019999999552965164, 'enableAntiFirefly': False, 'enableReprojectionTestSkippingWithoutMotion': True, 'enableMaterialTestForDiffuse': False})
    g.create_pass('NRDDeltaTransmission', 'NRD', {'enabled': True, 'method': 'RelaxDiffuse', 'outputSize': 'Default', 'worldSpaceMotion': False, 'disocclusionThreshold': 2.0, 'maxIntensity': 250.0, 'diffusePrepassBlurRadius': 16.0, 'diffuseMaxAccumulatedFrameNum': 31, 'diffuseMaxFastAccumulatedFrameNum': 2, 'diffusePhiLuminance': 2.0, 'diffuseLobeAngleFraction': 0.800000011920929, 'diffuseHistoryRejectionNormalThreshold': 0.0, 'disocclusionFixEdgeStoppingNormalPower': 8.0, 'disocclusionFixMaxRadius': 32.0, 'disocclusionFixNumFramesToFix': 4, 'historyClampingColorBoxSigmaScale': 2.0, 'spatialVarianceEstimationHistoryThreshold': 4, 'atrousIterationNum': 6, 'minLuminanceWeight': 0.0, 'depthThreshold': 0.019999999552965164, 'enableAntiFirefly': False, 'enableReprojectionTestSkippingWithoutMotion': True, 'enableMaterialTestForDiffuse': False})
    g.create_pass('NRDReflectionMotionVectors', 'NRD', {'enabled': True, 'method': 'SpecularReflectionMv', 'outputSize': 'Default', 'worldSpaceMotion': False, 'disocclusionThreshold': 2.0, 'maxIntensity': 1000.0})
    g.create_pass('NRDTransmissionMotionVectors', 'NRD', {'enabled': True, 'method': 'SpecularDeltaMv', 'outputSize': 'Default', 'worldSpaceMotion': False, 'disocclusionThreshold': 2.0, 'maxIntensity': 1000.0})
    g.create_pass('ModulateIllumination', 'ModulateIllumination', {'useEmission': True, 'useDiffuseReflectance': True, 'useDiffuseRadiance': True, 'useSpecularReflectance': True, 'useSpecularRadiance': True, 'useDeltaReflectionEmission': True, 'useDeltaReflectionReflectance': True, 'useDeltaReflectionRadiance': True, 'useDeltaTransmissionEmission': True, 'useDeltaTransmissionReflectance': True, 'useDeltaTransmissionRadiance': True, 'useResidualRadiance': False, 'outputSize': 'Default'})
    g.create_pass('DLSS', 'DLSSPass', {'enabled': True, 'outputSize': 'Default', 'profile': 'Balanced', 'motionVectorScale': 'Relative', 'isHDR': True, 'sharpness': 0.0, 'exposure': 0.0})
    g.create_pass('ToneMapperNRD', 'ToneMapper', {'outputSize': 'Default', 'useSceneMetadata': True, 'exposureCompensation': 0.0, 'autoExposure': False, 'filmSpeed': 100.0, 'whiteBalance': False, 'whitePoint': 6500.0, 'operator': 'Aces', 'clamp': True, 'whiteMaxLuminance': 1.0, 'whiteScale': 11.199999809265137, 'fNumber': 1.0, 'shutter': 1.0, 'exposureMode': 'AperturePriority'})
    g.add_edge('GBufferRT.vbuffer', 'PathTracer.vbuffer')
    g.add_edge('GBufferRT.viewW', 'PathTracer.viewW')
    g.add_edge('PathTracer.color', 'AccumulatePass.input')
    g.add_edge('AccumulatePass.output', 'ToneMapperReference.src')
    g.add_edge('PathTracer.nrdDiffuseRadianceHitDist', 'NRDDiffuseSpecular.diffuseRadianceHitDist')
    g.add_edge('PathTracer.nrdSpecularRadianceHitDist', 'NRDDiffuseSpecular.specularRadianceHitDist')
    g.add_edge('GBufferRT.mvecW', 'NRDDiffuseSpecular.mvec')
    g.add_edge('GBufferRT.normWRoughnessMaterialID', 'NRDDiffuseSpecular.normWRoughnessMaterialID')
    g.add_edge('GBufferRT.linearZ', 'NRDDiffuseSpecular.viewZ')
    g.add_edge('PathTracer.nrdDeltaReflectionHitDist', 'NRDReflectionMotionVectors.specularHitDist')
    g.add_edge('GBufferRT.linearZ', 'NRDReflectionMotionVectors.viewZ')
    g.add_edge('GBufferRT.normWRoughnessMaterialID', 'NRDReflectionMotionVectors.normWRoughnessMaterialID')
    g.add_edge('GBufferRT.mvec', 'NRDReflectionMotionVectors.mvec')
    g.add_edge('PathTracer.nrdDeltaReflectionRadianceHitDist', 'NRDDeltaReflection.diffuseRadianceHitDist')
    g.add_edge('NRDReflectionMotionVectors.reflectionMvec', 'NRDDeltaReflection.mvec')
    g.add_edge('PathTracer.nrdDeltaReflectionNormWRoughMaterialID', 'NRDDeltaReflection.normWRoughnessMaterialID')
    g.add_edge('PathTracer.nrdDeltaReflectionPathLength', 'NRDDeltaReflection.viewZ')
    g.add_edge('GBufferRT.posW', 'NRDTransmissionMotionVectors.deltaPrimaryPosW')
    g.add_edge('PathTracer.nrdDeltaTransmissionPosW', 'NRDTransmissionMotionVectors.deltaSecondaryPosW')
    g.add_edge('GBufferRT.mvec', 'NRDTransmissionMotionVectors.mvec')
    g.add_edge('PathTracer.nrdDeltaTransmissionRadianceHitDist', 'NRDDeltaTransmission.diffuseRadianceHitDist')
    g.add_edge('NRDTransmissionMotionVectors.deltaMvec', 'NRDDeltaTransmission.mvec')
    g.add_edge('PathTracer.nrdDeltaTransmissionNormWRoughMaterialID', 'NRDDeltaTransmission.normWRoughnessMaterialID')
    g.add_edge('PathTracer.nrdDeltaTransmissionPathLength', 'NRDDeltaTransmission.viewZ')
    g.add_edge('PathTracer.nrdEmission', 'ModulateIllumination.emission')
    g.add_edge('PathTracer.nrdDiffuseReflectance', 'ModulateIllumination.diffuseReflectance')
    g.add_edge('NRDDiffuseSpecular.filteredDiffuseRadianceHitDist', 'ModulateIllumination.diffuseRadiance')
    g.add_edge('PathTracer.nrdSpecularReflectance', 'ModulateIllumination.specularReflectance')
    g.add_edge('NRDDiffuseSpecular.filteredSpecularRadianceHitDist', 'ModulateIllumination.specularRadiance')
    g.add_edge('PathTracer.nrdDeltaReflectionEmission', 'ModulateIllumination.deltaReflectionEmission')
    g.add_edge('PathTracer.nrdDeltaReflectionReflectance', 'ModulateIllumination.deltaReflectionReflectance')
    g.add_edge('NRDDeltaReflection.filteredDiffuseRadianceHitDist', 'ModulateIllumination.deltaReflectionRadiance')
    g.add_edge('PathTracer.nrdDeltaTransmissionEmission', 'ModulateIllumination.deltaTransmissionEmission')
    g.add_edge('PathTracer.nrdDeltaTransmissionReflectance', 'ModulateIllumination.deltaTransmissionReflectance')
    g.add_edge('NRDDeltaTransmission.filteredDiffuseRadianceHitDist', 'ModulateIllumination.deltaTransmissionRadiance')
    g.add_edge('PathTracer.nrdResidualRadianceHitDist', 'ModulateIllumination.residualRadiance')
    g.add_edge('GBufferRT.mvec', 'DLSS.mvec')
    g.add_edge('GBufferRT.linearZ', 'DLSS.depth')
    g.add_edge('ModulateIllumination.output', 'DLSS.color')
    g.add_edge('DLSS.output', 'ToneMapperNRD.src')
    g.mark_output('ToneMapperNRD.dst')
    g.mark_output('ToneMapperReference.dst')
    return g
m.addGraph(render_graph_PathTracerNRD())
from pathlib import WindowsPath, PosixPath
from falcor import *

def render_graph_PathTracer():
    g = RenderGraph('PathTracer')
    g.create_pass('PathTracer', 'PathTracer', {'samplesPerPixel': 1, 'maxSurfaceBounces': 10, 'maxDiffuseBounces': 3, 'maxSpecularBounces': 3, 'maxTransmissionBounces': 10, 'sampleGenerator': 0, 'useBSDFSampling': True, 'useRussianRoulette': False, 'useNEE': True, 'useMIS': True, 'misHeuristic': 'Balance', 'misPowerExponent': 2.0, 'emissiveSampler': 'LightBVH', 'lightBVHOptions': {'buildOptions': {'splitHeuristicSelection': 'BinnedSAOH', 'maxTriangleCountPerLeaf': 10, 'binCount': 16, 'volumeEpsilon': 0.0010000000474974513, 'splitAlongLargest': False, 'useVolumeOverSA': False, 'useLeafCreationCost': True, 'createLeavesASAP': True, 'allowRefitting': True, 'usePreintegration': True, 'useLightingCones': True}, 'useBoundingCone': True, 'useLightingCone': True, 'disableNodeFlux': False, 'useUniformTriangleSampling': True, 'solidAngleBoundMethod': 'Sphere'}, 'useRTXDI': False, 'RTXDIOptions': {'mode': 'SpatiotemporalResampling', 'presampledTileCount': 128, 'presampledTileSize': 1024, 'storeCompactLightInfo': True, 'localLightCandidateCount': 24, 'infiniteLightCandidateCount': 8, 'envLightCandidateCount': 8, 'brdfCandidateCount': 1, 'brdfCutoff': 0.0, 'testCandidateVisibility': True, 'biasCorrection': 'Basic', 'depthThreshold': 0.10000000149011612, 'normalThreshold': 0.5, 'samplingRadius': 30.0, 'spatialSampleCount': 1, 'spatialIterations': 5, 'maxHistoryLength': 20, 'boilingFilterStrength': 0.0, 'rayEpsilon': 0.0010000000474974513, 'useEmissiveTextures': False, 'enableVisibilityShortcut': False, 'enablePermutationSampling': False}, 'useAlphaTest': True, 'adjustShadingNormals': False, 'maxNestedMaterials': 2, 'useLightsInDielectricVolumes': False, 'disableCaustics': False, 'specularRoughnessThreshold': 0.25, 'primaryLodMode': 'Mip0', 'lodBias': 0.0, 'useNRDDemodulation': True, 'outputSize': 'Default', 'colorFormat': 'LogLuvHDR'})
    g.create_pass('VBufferRT', 'VBufferRT', {'outputSize': 'Default', 'samplePattern': 'Stratified', 'sampleCount': 16, 'useAlphaTest': True, 'adjustShadingNormals': True, 'forceCullMode': False, 'cull': 'Back', 'useTraceRayInline': False, 'useDOF': True})
    g.create_pass('AccumulatePass', 'AccumulatePass', {'enabled': True, 'outputSize': 'Default', 'autoReset': True, 'precisionMode': 'Single', 'maxFrameCount': 0, 'overflowMode': 'Stop'})
    g.create_pass('ToneMapper', 'ToneMapper', {'outputSize': 'Default', 'useSceneMetadata': True, 'exposureCompensation': 0.0, 'autoExposure': False, 'filmSpeed': 100.0, 'whiteBalance': False, 'whitePoint': 6500.0, 'operator': 'Aces', 'clamp': True, 'whiteMaxLuminance': 1.0, 'whiteScale': 11.199999809265137, 'fNumber': 1.0, 'shutter': 1.0, 'exposureMode': 'AperturePriority'})
    g.add_edge('VBufferRT.vbuffer', 'PathTracer.vbuffer')
    g.add_edge('VBufferRT.viewW', 'PathTracer.viewW')
    g.add_edge('VBufferRT.mvec', 'PathTracer.mvec')
    g.add_edge('PathTracer.color', 'AccumulatePass.input')
    g.add_edge('AccumulatePass.output', 'ToneMapper.src')
    g.mark_output('ToneMapper.dst')
    return g
m.addGraph(render_graph_PathTracer())
from pathlib import WindowsPath, PosixPath
from falcor import *

def render_graph_RTXDI():
    g = RenderGraph('RTXDI')
    g.create_pass('VBufferRT', 'VBufferRT', {'outputSize': 'Default', 'samplePattern': 'Center', 'sampleCount': 16, 'useAlphaTest': True, 'adjustShadingNormals': True, 'forceCullMode': False, 'cull': 'Back', 'useTraceRayInline': False, 'useDOF': True})
    g.create_pass('RTXDIPass', 'RTXDIPass', {'options': {'mode': 'SpatiotemporalResampling', 'presampledTileCount': 128, 'presampledTileSize': 1024, 'storeCompactLightInfo': True, 'localLightCandidateCount': 24, 'infiniteLightCandidateCount': 8, 'envLightCandidateCount': 8, 'brdfCandidateCount': 1, 'brdfCutoff': 0.0, 'testCandidateVisibility': True, 'biasCorrection': 'Basic', 'depthThreshold': 0.10000000149011612, 'normalThreshold': 0.5, 'samplingRadius': 30.0, 'spatialSampleCount': 1, 'spatialIterations': 5, 'maxHistoryLength': 20, 'boilingFilterStrength': 0.0, 'rayEpsilon': 0.0010000000474974513, 'useEmissiveTextures': False, 'enableVisibilityShortcut': False, 'enablePermutationSampling': False}})
    g.create_pass('AccumulatePass', 'AccumulatePass', {'enabled': False, 'outputSize': 'Default', 'autoReset': True, 'precisionMode': 'Single', 'maxFrameCount': 0, 'overflowMode': 'Stop'})
    g.create_pass('ToneMapper', 'ToneMapper', {'outputSize': 'Default', 'useSceneMetadata': True, 'exposureCompensation': 0.0, 'autoExposure': False, 'filmSpeed': 100.0, 'whiteBalance': False, 'whitePoint': 6500.0, 'operator': 'Aces', 'clamp': True, 'whiteMaxLuminance': 1.0, 'whiteScale': 11.199999809265137, 'fNumber': 1.0, 'shutter': 1.0, 'exposureMode': 'AperturePriority'})
    g.add_edge('VBufferRT.vbuffer', 'RTXDIPass.vbuffer')
    g.add_edge('VBufferRT.mvec', 'RTXDIPass.mvec')
    g.add_edge('RTXDIPass.color', 'AccumulatePass.input')
    g.add_edge('AccumulatePass.output', 'ToneMapper.src')
    g.mark_output('ToneMapper.dst')
    return g
m.addGraph(render_graph_RTXDI())

# Scene
m.loadScene('Arcade/Arcade.fbx')
m.scene.renderSettings = SceneRenderSettings(useEnvLight=True, useAnalyticLights=True, useEmissiveLights=True, useGridVolumes=True, diffuseAlbedoMultiplier=1)
m.scene.camera.position = float3(-0.574564, 1.535029, 1.067791)
m.scene.camera.target = float3(-0.198715, 1.236241, 0.190600)
m.scene.camera.up = float3(0.000409, 0.999999, -0.000955)
m.scene.cameraSpeed = 1.0

# Window Configuration
m.resizeFrameBuffer(1274, 919)
m.ui = True

# Clock Settings
m.clock.time = 0
m.clock.framerate = 0
# If framerate is not zero, you can use the frame property to set the start frame
# m.clock.frame = 0

# Frame Capture
m.frameCapture.outputDir = '.'
m.frameCapture.baseFilename = 'Mogwai'

