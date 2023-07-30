import FreeCAD as App
import FreeCADGui as Gui
from PySide import QtGui
import Part
import Draft

def add_local_axes():
    # Get the active document
    doc = App.ActiveDocument

    # Check if XYZ axis representations already exist, delete them if they do
    if doc:
        for obj in doc.Objects:
            if obj.isDerivedFrom("App::DocumentObjectGroup"):
                if obj.Label == "Datum_Plane_Axis":
                    # Delete the child objects
                    for child_obj in obj.Group:
                        doc.removeObject(child_obj.Name)
                    # Delete the folder
                    doc.removeObject(obj.Name)

    # Check if a datum plane is selected in the tree view
    if doc and Gui.Selection.getSelectionEx():
        selection = Gui.Selection.getSelectionEx()
        if selection and isinstance(selection[0].SubObjects[0], Part.Face):
            datum_plane = selection[0].SubObjects[0]
            placement = datum_plane.Placement

            # Create a folder to group the axis representations
            folder = doc.addObject("App::DocumentObjectGroup", "Datum_Plane_Axes")

            # Create small axis representations
            size =50.0  # Size of the axis representations

            # Create Draft objects for the axis
            x_axis = Draft.makeLine(App.Vector(0, 0, 0), App.Vector(size, 0, 0))
            y_axis = Draft.makeLine(App.Vector(0, 0, 0), App.Vector(0, size, 0))
            z_axis = Draft.makeLine(App.Vector(0, 0, 0), App.Vector(0, 0, size))

            # Set the placements for the axis representations
            x_axis.Placement = placement
            y_axis.Placement = placement
            z_axis.Placement = placement

            # Set the display mode of the axis representations to "Wireframe"
            x_axis.ViewObject.DisplayMode = "Wireframe"
            y_axis.ViewObject.DisplayMode = "Wireframe"
            z_axis.ViewObject.DisplayMode = "Wireframe"

            # Set the colors of the axis representations
            x_axis.ViewObject.LineColor = (1.0, 0.0, 0.0)  # Red for X-axis
            y_axis.ViewObject.LineColor = (0.0, 1.0, 0.0)  # Green for Y-axis
            z_axis.ViewObject.LineColor = (0.0, 0.0, 1.0)  # Blue for Z-axis

            # Add the axis representations as child objects to the folder
            folder.addObject(x_axis)
            folder.addObject(y_axis)
            folder.addObject(z_axis)

            # Add the folder to the active document
            doc.addObject(folder)

            # Refresh the document and the 3D view
            App.ActiveDocument.recompute()
            Gui.SendMsgToActiveView("ViewFit")

# Call the function to add or clear local axis representations
add_local_axes()
