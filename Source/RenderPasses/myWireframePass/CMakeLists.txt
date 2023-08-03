add_plugin(myWireframePass)

target_sources(myWireframePass PRIVATE
    myWireframePass.cpp
    myWireframePass.h
)

target_source_group(myWireframePass "RenderPasses")
