from pathlib import WindowsPath, PosixPath
from falcor import *

def render_graph_DefaultRenderGraph():
    g = RenderGraph('DefaultRenderGraph')
    g.create_pass('ImageLoader', 'ImageLoader', {'outputSize': 'Default', 'outputFormat': 'BGRA8UnormSrgb', 'filename': 'C:\\Users\\jasperyin\\Pictures\\Saved Pictures\\FvCeifEaUAAvVLG.png', 'mips': False, 'srgb': True, 'arrayIndex': 0, 'mipLevel': 0})
    g.create_pass('myRenderLibrary', 'myRenderLibrary', {})
    g.add_edge('ImageLoader.dst', 'myRenderLibrary.input')
    g.mark_output('myRenderLibrary.output')
    return g

DefaultRenderGraph = render_graph_DefaultRenderGraph()
try: m.addGraph(DefaultRenderGraph)
except NameError: None
