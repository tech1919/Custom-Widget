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

    
    if "ArcGISWebAppBuilder" in os.listdir(arc_folder):
        arc_folder = os.path.join(arc_folder , "ArcGISWebAppBuilder")




    print(Fore.CYAN + "Choose one of the widgets below : " + colorama.Style.RESET_ALL)
    
    widget_name_list = []

    for widget in os.listdir(os.getcwd()):
        if ".exe" in widget or ".py" in widget or ".md" in widget or "git" in widget:
            continue

        widget_name_list.append(widget)

    for index , widget in enumerate(widget_name_list):
        print(f"    {index+1}. {widget}")

    print()
    widget_number = int(input(Fore.CYAN + "Enter widget number :" + colorama.Style.RESET_ALL))
    widget_number -= 1
    widget_name = widget_name_list[widget_number]
    print(Fore.CYAN + f"Updating Widget : {widget_name}" + colorama.Style.RESET_ALL)
    
    widget_default_uri = f"widgets/{widget_name}/Widget"
    widgets_folder = os.path.join(arc_folder , "client\stemapp3d\widgets")
    if not os.path.exists(widgets_folder):
        raise Exception(Fore.RED + f"could not locate {widgets_folder} folder" + colorama.Style.RESET_ALL)
    
    config_json_file = os.path.join(arc_folder , "client\stemapp3d\predefined-apps\default\config.json")
    if not os.path.exists(config_json_file):
        print(Fore.RED + "could not locate config.json file" + colorama.Style.RESET_ALL)
    
    if widget_name in os.listdir(widgets_folder):
        answer = input(f"Do you want to update the {widget_name}? [Y/N] ")
        if answer.lower() == "y":
            answer = True
        elif answer.lower() == "n":
            answer = False

        if answer:
            shutil.rmtree(
                os.path.join(widgets_folder , widget_name)
            )
            shutil.copytree(
                src= os.path.join(os.getcwd() , widget_name),
                dst=os.path.join(widgets_folder , widget_name)
                )
    else:
        shutil.copytree(
                src= os.path.join(os.getcwd() , widget_name),
                dst=os.path.join(widgets_folder , widget_name)
                )


if __name__ == "__main__":
    main()