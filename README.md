# Limitations Widget - arcgis web app builder

### Idea
This widget will limit the scene, according to the admin. 
such as tilt, zoom.. 
  

### implementation

1) dowmload the LimitationsPinkas folder from this repo.
2) extract to this path: 
    ```
    "...\ArcGISWebAppBuilder\client\stemapp3d\widgets"
    ```

3) Open `config.json` file:

    ```
    "...\ArcGISWebAppBuilder\client\stemapp3d\predefined-apps\default\config.json"
    ```
4) add this line under the `"widgets"` array:
    ```
    {
      "uri": "widgets/LimitationsPinkas/Widget"
    }
    ```
