from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Marks data (embedded here directly)
marks_data = [{"name":"3cNr3ZTsSO","marks":2},{"name":"DdT","marks":26},{"name":"N","marks":30},{"name":"wIpXM1OF","marks":93},{"name":"arKJ","marks":79},{"name":"0","marks":97},{"name":"hLmwja8Qe","marks":70},{"name":"w","marks":72},{"name":"zJpe","marks":40},{"name":"reASnUc","marks":78},{"name":"A","marks":53},{"name":"Z42yG5t","marks":78},{"name":"xOXLW","marks":57},{"name":"0QoES5w9","marks":39},{"name":"kx3VcUFgR","marks":62},{"name":"Xv","marks":4},{"name":"2j7gJ","marks":19},{"name":"mIzdgCBd","marks":97},{"name":"Vuu2t","marks":72},{"name":"GFbeKn6Cb0","marks":13},{"name":"Cej2F5Nz","marks":90},{"name":"wgPjDE3egv","marks":93},{"name":"8dWp33xji","marks":41},{"name":"Az3RBnD0","marks":35},{"name":"JUjstG5","marks":41},{"name":"y0","marks":89},{"name":"9f","marks":62},{"name":"4LxuHNyEhd","marks":94},{"name":"k","marks":49},{"name":"5Z4BVvjbAd","marks":77},{"name":"vq","marks":81},{"name":"10o3zRgCO","marks":60},{"name":"Un8XNbp","marks":26},{"name":"bTbc","marks":0},{"name":"1U64PO2","marks":64},{"name":"OeZ2lmxzC","marks":32},{"name":"TvQXG","marks":14},{"name":"wjaciIxe","marks":9},{"name":"pm","marks":46},{"name":"c","marks":45},{"name":"FfX3gPHc1r","marks":93},{"name":"jweh","marks":3},{"name":"KNis","marks":4},{"name":"wxaXrGqHI","marks":72},{"name":"tkqXOwct3A","marks":24},{"name":"ug5jNuy","marks":99},{"name":"rlWH0L","marks":53},{"name":"ybR","marks":37},{"name":"cUaVfgqL","marks":96},{"name":"9KQ","marks":67},{"name":"zvEUEWTFc0","marks":64},{"name":"rWD7oeHwdi","marks":28},{"name":"nPzNpso","marks":75},{"name":"MErn","marks":89},{"name":"HLe2EWIh","marks":9},{"name":"JIQa","marks":98},{"name":"0LXiJG6H","marks":54},{"name":"JHyvvo","marks":93},{"name":"Ga5Zh2KT","marks":13},{"name":"r3BxuBh","marks":95},{"name":"OqenVRCW","marks":36},{"name":"GPxvl5cw","marks":59},{"name":"mi4aZqhv","marks":15},{"name":"9eylOUmfxt","marks":84},{"name":"If0v","marks":13},{"name":"9","marks":71},{"name":"C","marks":39},{"name":"WP3","marks":46},{"name":"I3PCY","marks":40},{"name":"NE","marks":61},{"name":"ijHQZsll1","marks":91},{"name":"h2y94BM","marks":42},{"name":"K1Ts","marks":72},{"name":"LGlJ38R8oO","marks":53},{"name":"Nxr84aS","marks":47},{"name":"JGhe","marks":96},{"name":"5Lq5W","marks":77},{"name":"WRvf0GyNt7","marks":35},{"name":"oFpo4nRnz","marks":82},{"name":"g","marks":19},{"name":"yH","marks":42},{"name":"TO6M","marks":38},{"name":"BluN","marks":66},{"name":"9MAKNONKH","marks":14},{"name":"3Te41VNC4","marks":37},{"name":"Qsv3R","marks":61},{"name":"kjBOJwf","marks":98},{"name":"UIr9F3","marks":8},{"name":"D3EyUzu","marks":4},{"name":"MLqAHDd1","marks":51},{"name":"Ga1Yh8Jzdc","marks":75},{"name":"2eezZtV","marks":97},{"name":"RvDSi","marks":85},{"name":"CQZbJptP","marks":37},{"name":"unr4Xm3u","marks":86},{"name":"5cSqUtXcj","marks":10},{"name":"4h4g","marks":76},{"name":"75jVsAGm","marks":46},{"name":"y6","marks":8},{"name":"khNc3vXRHQ","marks":79}]


# Build lookup dictionary
marks_lookup = {entry["name"]: entry["marks"] for entry in marks_data}

@app.get("/api")
async def get_marks(name: list[str] = []):
    result = []
    for n in name:
        result.append(marks_lookup.get(n, None))  # None if not found
    return {"marks": result}
