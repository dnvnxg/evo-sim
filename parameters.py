class ParamManager:
    width = int
    height = int
    population = int
    graphicsScaleFactor = int


    def __init__(self,
                 width=200,
                 height=200,
                 graphicsScaleFactor=2,
                 ) -> None:
        self.width = width
        self.height = height
        self.graphicsScaleFactor = graphicsScaleFactor