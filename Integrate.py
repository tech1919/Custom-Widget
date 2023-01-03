import os
import json
import shutil
import colorama
colorama.init()
from colorama import Fore


def main():

    print(Fore.CYAN + "Costum WebAppbuilder Widgets" + colorama.Style.RESET_ALL)
    print()

    arc_folder = input(Fore.GREEN + "Enter path to the location of ArcGISWebAppBuilder folder : " + colorama.Style.RESET_ALL)

    # get the location of the ArcGISWebAppBuilder folder
    if not "ArcGISWebAppBuilder" in arc_folder:
        arc_folder = os.path.join(arc_folder , "ArcGISWebAppBuilder")

    print(Fore.CYAN + arc_folder  + colorama.Style.RESET_ALL)
    if not os.path.exists(arc_folder):
        raise Exception(Fore.RED + f"could not locate {arc_folder} folder" + colorama.Style.RESET_ALL)
        

    # collect the list of widgets from this folder
    widget_name_list = []
    for widget in os.listdir(os.getcwd()):
        if ".exe" in widget or ".py" in widget or ".md" in widget or "git" in widget:
            continue
        widget_name_list.append(widget)

    # get user's choise
    print(Fore.CYAN + "Choose one of the widgets below : " + colorama.Style.RESET_ALL)
    for index , widget in enumerate(widget_name_list):
        print(f"    {index+1}. {widget}")
    print()
    widget_number = int(input(Fore.CYAN + "Enter widget number and press Enter : " + colorama.Style.RESET_ALL))
    widget_number -= 1
    widget_name = widget_name_list[widget_number]
    print(Fore.CYAN + f"Updating Widget : {widget_name}" + colorama.Style.RESET_ALL)
    

    # get the widget folder in ArcGISWebAppBuilder
    widgets_folder = os.path.join(arc_folder , "client\stemapp3d\widgets")
    if not os.path.exists(widgets_folder):
        raise Exception(Fore.RED + f"could not locate {widgets_folder} folder" + colorama.Style.RESET_ALL)
    
    # copy the widget folder to the desired folder
    if widget_name in os.listdir(widgets_folder):
        answer = input(Fore.GREEN + f"Seems like this widget is already in use. Do you want to update {widget_name}? [Y/N] " + colorama.Style.RESET_ALL)
        if answer.lower() == "y" or "yes" == answer.lower():
            answer = True
        elif answer.lower() == "n":
            answer = False
        else:
            answer = False

        if answer:
            try:
                shutil.rmtree(
                    os.path.join(widgets_folder , widget_name)
                )
            except:
                raise Exception(Fore.RED + f"Error while removing the {widget_name} widget" + colorama.Style.RESET_ALL)
            try:
                shutil.copytree(
                    src= os.path.join(os.getcwd() , widget_name),
                    dst=os.path.join(widgets_folder , widget_name)
                    )
            except:
                raise Exception(Fore.RED + f"Error while updating the {widget_name} widget" + colorama.Style.RESET_ALL)
    else:
        try:
            shutil.copytree(
                    src= os.path.join(os.getcwd() , widget_name),
                    dst=os.path.join(widgets_folder , widget_name)
                    )
        except:
            raise Exception(Fore.RED + f"Error while updating the {widget_name} widget" + colorama.Style.RESET_ALL)
        
    
    # check if this is a default widget
    if "default_widget.txt" in os.listdir(os.path.join(widgets_folder , widget_name)):
        
        answer = input(Fore.GREEN + f"Do you want to set {widget_name} as a default widget? [Y/N] " + colorama.Style.RESET_ALL)
        
        if "y" == answer.lower() or "yes" == answer.lower():

            

            config_json_file = os.path.join(arc_folder , "client\stemapp3d\predefined-apps\default\config.json")
            if not os.path.exists(config_json_file):
                raise Exception(Fore.RED + "could not locate config.json file" + colorama.Style.RESET_ALL)

            with open(config_json_file , "r") as f:
                config_data = f.read()
                config_data = json.loads(config_data)

            # update data
            widget_default_uri = f"widgets/{widget_name}/Widget"
            for index , uri in enumerate(config_data["widgetOnScreen"]["widgets"]):
                if uri["uri"] == widget_default_uri:
                    config_data["widgetOnScreen"]["widgets"].pop(index)

            config_data["widgetOnScreen"]["widgets"].append({"uri" : widget_default_uri})
            config_data = json.dumps(config_data)

            with open(config_json_file , "w") as f:
                f.write(config_data)


    print(Fore.GREEN + f"Widget {widget_name} was updated!" + colorama.Style.RESET_ALL)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    input("Press Enter to close this window...")