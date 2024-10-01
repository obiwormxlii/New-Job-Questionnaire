import rhinoscriptsyntax as rs
import json


def switchLayer(layerName, parentLayer=None):
    if rs.IsLayer(layerName):
        rs.CurrentLayer(layerName)
    else:
        if parentLayer is None:
            rs.AddLayer(layerName)
        else:
            rs.AddLayer(layerName, parentLayer)
        rs.CurrentLayer(layerName)


class BiminiLayoutTemplate:
    pocket = {"shape": str, "cutouts": bool}
    main = {"window": bool, "stayCutout": bool}
    notes = str

    def __init__(self, biminiOptions, biminiCount=0):
        startingLayer = rs.CurrentLayer()
        switchLayer("Layout", "Document")

        self.pocket["shape"] = biminiOptions["pocket"]["shape"]
        if biminiOptions["pocket"]["cutouts"] == True:
            self.pocket["cutouts"] = "Yes"
        else:
            self.pocket["cutouts"] = "No"
        if biminiOptions["main"]["window"] == True:
            self.main["window"] = "Yes"
        else:
            self.main["window"] = "No"
        if biminiOptions["main"]["stayCutout"] == True:
            self.main["stayCutout"] = "Yes"
        else:
            self.main["stayCutout"] = "No"
        self.notes = biminiOptions["notes"]

        rectangleWidth = 170
        rectangleHeight = 50

        rectangleOrigin = ((-1 * rectangleWidth / 2), biminiCount * rectangleHeight, 0)
        rectangleX = rs.PointAdd(rectangleOrigin, (1, 0, 0))
        rectangleY = rs.PointAdd(rectangleOrigin, (0, 1, 0))

        rectanglePlane = rs.PlaneFromPoints(rectangleOrigin, rectangleX, rectangleY)
        rectangle = rs.AddRectangle(rectanglePlane, rectangleWidth, rectangleHeight)

        groupName = "Bimini" + str(rectangle)
        rs.AddGroup(groupName)

        text = "BIMINI " + str(biminiCount + 1) + "\n" "    Pocket: " + self.pocket[
            "shape"
        ] + "\n    Cutouts: " + str(self.pocket["cutouts"]) + "\n    Window: " + str(
            self.main["window"]
        ) + "\n    Stay Cutout: " + str(
            self.main["stayCutout"]
        )

        biminiInfo = rs.AddText(
            text, rs.PointAdd(rectangleOrigin, (0 + 2, rectangleHeight - 2, 0)), 0.125
        )
        notes = rs.AddText(
            "Notes: " + self.notes,
            rs.PointAdd(rectangleOrigin, (2, 2, 0)),
            0.125,
            justification=65536,
        )
        rs.AddObjectsToGroup([rectangle, biminiInfo, notes], groupName)

        switchLayer(startingLayer)


class WindowLayoutTemplate:
    windowStyle = str
    glassType = str
    attachmentType = {
        "top": str,
        "bottom": str,
        "leftSide": str,
        "rightSide": str,
    }
    sideStyle = {
        "left": str,
        "right": str,
    }
    features = {
        "smiles": bool,
        "vents": bool,
        "burnStrips": bool,
        "cutouts": bool,
        "cinchStraps": bool,
    }

    def __init__(self, windowOptions, windowCount, windowIndex):

        # Set up Layers
        startingLayer = rs.CurrentLayer()
        switchLayer("Layout", "Document")

        # define window options

        self.windowStyle = windowOptions["windowStyle"]
        self.glassType = windowOptions["glassType"]

        # define attachment options
        self.attachmentType["top"] = windowOptions["attachmentType"]["top"]
        self.attachmentType["bottom"] = windowOptions["attachmentType"]["bottom"]
        self.attachmentType["leftSide"] = windowOptions["attachmentType"]["leftSide"]
        self.attachmentType["rightSide"] = windowOptions["attachmentType"]["rightSide"]
        self.sideStyle["left"] = windowOptions["sideStyle"]["left"]
        self.sideStyle["right"] = windowOptions["sideStyle"]["right"]

        # layout box
        rectangleWidth = 64
        rectangleHeight = 64

        firstPosition = windowCount * rectangleWidth / 2 - rectangleWidth
        currentPosition = firstPosition - rectangleWidth * windowIndex

        rectangleOrigin = (currentPosition, -1 * rectangleHeight, 0)
        rectangleX = rs.PointAdd(rectangleOrigin, (1, 0, 0))
        rectangleY = rs.PointAdd(rectangleOrigin, (0, 1, 0))

        rectanglePlane = rs.PlaneFromPoints(rectangleOrigin, rectangleX, rectangleY)
        self.rectangle = rs.AddRectangle(
            rectanglePlane, rectangleWidth, rectangleHeight
        )

        # add group
        groupName = "Window" + str(self.rectangle)
        rs.AddGroup(groupName)

        # add text
        infoText = (
            "Window " + str(windowIndex + 1) + "\n\n"
            "Window Style: " + self.windowStyle + "\n"
            "Glass Type: " + self.glassType
        )

        if windowOptions["features"]["smiles"] == True:
            infoText = infoText + "\n" + "Smiles: Yes"

        if windowOptions["features"]["vents"] == True:
            infoText = infoText + "\n" + "Vents: Yes"

        if windowOptions["features"]["burnStrips"] == True:
            infoText = infoText + "\n" + "Burn Strips: Yes"

        if windowOptions["features"]["cutouts"] == True:
            infoText = infoText + "\n" + "Cutouts: Yes"

        if windowOptions["features"]["cinchStraps"] == True:
            infoText = infoText + "\n" + "Cinch Straps: Yes"

        topText = "Top: " + self.attachmentType["top"]
        topPosition = rs.PointAdd(
            rectangleOrigin, (rectangleWidth / 2, rectangleHeight - 2, 0)
        )

        bottomText = "Bottom: " + self.attachmentType["bottom"]
        bottomPosition = rs.PointAdd(rectangleOrigin, (rectangleWidth / 2, 2, 0))

        leftText = (
            "Left: "
            + self.sideStyle["left"]
            + "\n"
            + "Attachment: "
            + self.attachmentType["leftSide"]
        )
        leftPosition = rs.PointAdd(rectangleOrigin, (2, rectangleHeight / 2, 0))

        rightText = (
            "Right: "
            + self.sideStyle["right"]
            + "\n"
            + "Attachment: "
            + self.attachmentType["rightSide"]
        )
        rightPosition = rs.PointAdd(
            rectangleOrigin, (rectangleWidth - 2, rectangleHeight / 2, 0)
        )

        # add text objects
        windowInfo = rs.AddText(
            infoText,
            rs.PointAdd(rectangleOrigin, (0 + 2, rectangleHeight - 2, 0)),
            0.125,
        )
        topTextObject = rs.AddText(
            topText, topPosition, 0.125, justification=131072 + 2
        )
        bottomTextObject = rs.AddText(
            bottomText, bottomPosition, 0.125, justification=131072 + 2
        )
        leftTextObject = rs.AddText(
            leftText, leftPosition, 0.125, justification=131072 + 2
        )
        rightTextObject = rs.AddText(
            rightText, rightPosition, 0.125, justification=131072 + 2
        )

        # rotate text
        rs.RotateObject(leftTextObject, leftPosition, 90)
        rs.RotateObject(rightTextObject, rightPosition, 270)

        # add objects to group
        rs.AddObjectsToGroup(
            [
                self.rectangle,
                windowInfo,
                topTextObject,
                bottomTextObject,
                leftTextObject,
                rightTextObject,
            ],
            groupName,
        )

        # switch back to starting layer
        switchLayer(startingLayer)


def main():
    file = "Test_Test.json"

    with open(file) as f:
        try:
            data = json.load(f)
        except:
            data = {}

    if data.get("biminis"):
        biminis = data.get("biminis")
        for i in range(len(biminis)):
            biminiTemplate = BiminiLayoutTemplate(biminis[i], i)

    if data.get("windowPanels"):
        windowPanels = data.get("windowPanels")
        windowLayouts = []
        for i in range(len(windowPanels)):
            windowPanelTemplate = WindowLayoutTemplate(
                windowPanels[i], len(windowPanels), i
            )
            windowLayouts.append(windowPanelTemplate.rectangle)


if __name__ == "__main__":
    main()
