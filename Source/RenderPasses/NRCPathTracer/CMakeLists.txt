add_plugin(NRCPathTracer)

target_sources(NRCPathTracer PRIVATE
    Composite.cs.slang
    DataStructure.slang
    FalcorCUDA.cpp
    FalcorCUDA.h
    Helpers.h
    Network.cu
    Network.h
    NRC.cpp
    NRC.h
    NRC.slang
    NRCPathTracer.cpp
    NRCPathTracer.h
    NRCPathTracer.slang
    Parameters.h
    PathTracer.rt.slang
    PathTracer.slang

)

target_source_group(NRCPathTracer "RenderPasses")
