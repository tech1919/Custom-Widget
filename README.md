# ArcGISWebAppBuilder Costume Widgets

A library of custome widgets for the Web Appbuilder of ESRI

> ## Widgets

* [Limitations](./Limitations/) - Default 3D widget that apply limitation on the zoom and tilt of the SceneView.

> ## Integrate.exe
This file is an automation that allows a quick update of the widgets into the `ArcGISWebAppBuilder` folder.
For now, works for the 3D widgets.

**Basic use of the `Intagrate.exe` file:**

1. Download this repository with Git or as a zip folder. (if zipped, extract this repository) 
2. Run the `Integrate.exe` file. This should open a command line UI with this message:
```
Costum WebAppbuilder Widgets

Enter path to the location of ArcGISWebAppBuilder folder and press enter :
```
3. Enter the path where `ArcGISWebAppBuilder` foler located on your computer:
```
Enter path to the location of ArcGISWebAppBuilder folder : c:\...\ArcGISWebAppBuilder
```
4. You shold see a list of all the widgets from this library. Follow the instructions for updating the desired widget.
5. Run the Appbuilder to check if the widget has been added to the list from which you can choose.


**Without using the `Integrate.exe` file :**
1. Download this repository with Git or as a zip folder. (if zipped, extract this repository) 
2. Copy the Widget's folder to the `...\ArcGISWebAppBuilder\client\stemapp3d\widgets` with all the other 3D widgets.
3. Optional - to configure a widget to be a default widget, add the widget uri to the `...\ArcGISWebAppBuilder\client\stemapp3d\predefined-apps\default\config.json` as follows:

```
"widgetOnScreen": {
    "widgets":[
        {"uri" : "widgets/enter_widget_name_here/Widget"}
    ]
}
```
By adding it to this list, the widget will render as a default with all the other widgets from this list.

