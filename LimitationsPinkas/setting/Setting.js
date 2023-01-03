
define([
    'dojo/_base/declare',
    'jimu/BaseWidgetSetting'
  ],
  function(declare, BaseWidgetSetting) {
  
    //Please note that the widget depends on the 3.x API
  
    return declare([BaseWidgetSetting], {
      baseClass: 'jimu-widget-limited-setting',
  
      postCreate: function(){
        //the config object is passed in
        this.setConfig(this.config);
      },
  
      setConfig: function(config){
        this.textNode.value = config.configText;
        console.log("String setConfig: " + config.configText);
      },
  
      getConfig: function(){
        //WAB will get config object through this method
        return {
          configText: this.textNode.value
        };
      }
    });
  });