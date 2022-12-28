define(['dojo/_base/declare', 'jimu/BaseWidget','dojo/on', 'dojo/sniff'],
function(declare, BaseWidget) {
  //To create a widget, you need to derive from BaseWidget.
  return declare([BaseWidget], {
    name: 'limitations',

    startup: function(){
      var sceneElements = document.getElementsByClassName("esri-view-root");
      var zoomInButton = document.getElementsByClassName("esri-icon esri-icon-plus");

      zoomInButton[1].addEventListener('click',  (event) => {
        this._zoomLimited()
       });

      sceneElements[0].addEventListener('mousewheel', (event) => {
        this._zoomLimited()
      });

      sceneElements[0].addEventListener('dblclick', (event) => {
        this._zoomLimited()
      });

      sceneElements[0].addEventListener('click', (event) => {
        this._navigateLimited()
      });   
    },  
    _zoomLimited: function(){
      var currentZoom = Number(this.sceneView.zoom);
      var limitZoomValue = 20.5;
      var eventType = event.type;
      var limitFlag = 0; 

      switch(eventType){
        case  'click':
          limitFlag = 0;
          if(currentZoom > limitZoomValue){this.sceneView.zoom -= 1;}
          break;
        case 'dblclick':
          limitFlag = (event.deltaY == null)? 1 : 0 ;
          break;
        case 'mousewheel':
          limitFlag = (event.deltaY < 0)? 1 : 0 ;
          break;
      }

      if(currentZoom > limitZoomValue && limitFlag){
        this.sceneView.zoom = currentZoom;
      }
      
    },
    _navigateLimited: function(){
      var limitTiltValue = 65;
      var currentTilt = this.sceneView.camera.tilt;
      var newCam = this.sceneView.camera.clone();
      var positionX = this.sceneView.camera.position.x;
      var positionY = this.sceneView.camera.position.y;
      newCam.tilt = limitTiltValue;
      newCam.position.x = positionX;
      newCam.position.y = positionY;

      if(currentTilt > limitTiltValue){  
        this.sceneView.camera = newCam;
      }
    },
      
  }); 
});
