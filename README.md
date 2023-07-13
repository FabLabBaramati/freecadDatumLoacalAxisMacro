

This macro is designed for the FreeCAD and adds small X, Y, and Z axis representations on a selected datum plane in the GUI.

## Usage

1. Ensure you have the freecad 020.2 or LinkStage branch of FreeCAD installed on your system.
2. Open FreeCAD and create or open a document that contains a datum plane.
3. In the 3D view select the datum plane you want to add the local coordinate axes to.
4. Go to the Macros menu in the FreeCAD GUI and choose "Macro...".
5. Click on the "New" button to create a new macro.
6. Replace the default macro code with the code provided in this repository's macro file.
7. Save the macro and close the editor.
8. In the Macro menu, locate the newly created macro and click on it to execute it.
9. The macro will add small X, Y, and Z axis representations on the selected datum plane in the 3D view. The X-axis is represented in red, the Y-axis in green, and the Z-axis in blue.

To clear the axis representations, simply click on the macro again, and the representations will be removed.

## Workbench Customization

To add a custom icon for the macro:

1. Download the provided icon file ("Std_DatumPlanelocalaxis.svg") from this repository.
2. In the FreeCAD GUI, go to the "Macro" menu and choose "Macro...".
3. Select the macro and click on the "Edit" button.
4. In the editor, click on the "Icon" button and browse to the location of the downloaded icon file ("Std_DatumPlanelocalaxis.svg").
5. Save the macro and close the editor.
The macro will now have the custom icon associated with it in the Macro menu.


