import pathlib
import os
import tkinter
from tkinter import filedialog
from PIL import Image

base_path = pathlib.Path(__file__).parent.resolve()
create_folders_ind = ''
character_input = ''
create_flag_ind = ''
tag_input = ''
name_input = ''
ideology_input = ''
ideologies = ['d','c','f','n']
ideologies_full = ['democratic', 'communism', 'fascism', 'neutrality']
ideologies_sub = ['conservatism', 'marxism', 'gen_nazism', 'despotism']

while not (create_folders_ind =='y' or create_folders_ind == 'n'):
    create_folders_ind = input("Create folders (y/n)? ").lower()

path_array = ["common/country_tags","common/countries","common/characters","history/countries","history/units","localisation/english","gfx/flags/medium","gfx/flags/small","history/states"]

if create_folders_ind == 'y':
    for folder in path_array:
        os.makedirs(folder,exist_ok=True)

while not len(tag_input)==3 or not tag_input[0:1].isalpha():
    tag_input = str(input("Choose a tag: ")).upper()

while not len(name_input)>0:
    name_input = str(input("Choose a country name: "))
    
while not ideology_input in ideologies:
    ideology_input = str(input("Which ideology is your country of: Democratic (d); Communism (c); Fascism (f); Neutrality(n)? "))
    
ideology_num = ideologies.index(ideology_input)

tag_file = open(path_array[0]+'/02_countries.txt', "a")
tag_file.seek(0,0)
tag_file.write(tag_input+' = "countries/'+name_input+'.txt"\n')
tag_file.close()

country_file = open(path_array[1]+'/'+name_input+'.txt', "w")
country_file.write('graphical_culture = eastern_european_gfx \ngraphical_culture_2d = eastern_european_2d\n\ncolor = { 0 0 0 }')
country_file.close()

character_file = open(path_array[2]+'/'+tag_input+'_characters.txt', "w")
character_file.write('characters={\n}')
character_file.close()

history_file = open(path_array[3]+'/'+tag_input+' - '+name_input+'.txt', "w")
history_file.write('capital = 1\n\noob = "'+tag_input+'_1936"\n\nset_research_slots = 3\n\n#set_technology = {\n#}\n\n#recruit_character = \n\nset_politics = {\n\truling_party = '+ideologies_full[ideology_num]+'\n\tlast_election = "1936.1.1"\n\telection_frequency = 48\n\telections_allowed = yes\n}\n\nset_popularities = {\n\t'+ideologies_full[ideology_num]+' = 70\n\t'+ideologies_full[(ideology_num+1)%4]+' = 10\n\t'+ideologies_full[(ideology_num+2)%4]+' = 10\n\t'+ideologies_full[(ideology_num+3)%4]+' = 10\n}')
history_file.close()

oob_file = open(path_array[4]+'/'+tag_input+'_1936.txt', "w")
oob_file.write('division_template={\n}\nunits = {\n}')
oob_file.close()

loc_file = open(path_array[5]+'/'+tag_input+'_l_english.yml', "w")
loc_file.write('l_english:\n '+tag_input+': "'+name_input+'"\n '+tag_input+'_DEF: "'+name_input+'"\n '+tag_input+'_AJG: "'+name_input+'"')
loc_file.close()

while len(character_input) == 0:
    character_input_orig = input("Create a leader?\nEnter 'n' for No, or enter their name: ")
    character_input = character_input_orig.replace(' ', '_')
    character_input_tag = tag_input+'_'+(character_input.lower())

if not character_input.lower() == 'n':
    with open(path_array[2]+'/'+tag_input+'_characters.txt', "r") as character_file:
        character_file_data = character_file.read()
        character_file_data = character_file_data.replace('}', '\t'+character_input_tag+' = { \n\t\tname = '+character_input_tag+'\n\t\tportraits = {\n\t\t\tcivilian = {\n\t\t\t\tlarge = GFX_portrait_'+character_input_tag+'\n\t\t\t}\n\t\t}\n\t\tcountry_leader = {\n\t\t\tideology = '+ideologies_sub[ideology_num]+'\n\t\t\texpire = "1960.1.1.1"\n\t\t\tid = -1\n\t\t}\n\t}\n}')
    with open(path_array[2]+'/'+tag_input+'_characters.txt', "w") as character_file:
        character_file.write(character_file_data)
    
    with open(path_array[3]+'/'+tag_input+' - '+name_input+'.txt', "r") as history_file:
        history_file_data = history_file.read()
    history_file_data = history_file_data.replace('#recruit_character =', 'recruit_character = '+character_input_tag)
    with open(path_array[3]+'/'+tag_input+' - '+name_input+'.txt', "w") as history_file:
        history_file.write(history_file_data)

    with open(path_array[5]+'/'+tag_input+'_l_english.yml', "a") as loc_file:
        loc_file.write('\n '+character_input_tag+': "'+character_input_orig+'"\n '+character_input_tag+'_desc: "'+character_input_orig+' Description"')

while not (create_flag_ind =='y' or create_flag_ind == 'n'):
    create_flag_ind = input("Use existing .png, .jpg or .tga file to create flags (y/n)? ")

if create_flag_ind == 'y':
    tkinter.Tk().withdraw()
    flag_input = filedialog.askopenfilename(initialdir = "/",title = "Select a Flag",filetypes = (("PNG files","*.png*"),("JPG files","*.jpg*"),("TGA files","*.tga*")))
    flag_orig = Image.open(flag_input)
    
    flag_large = flag_orig.resize((82, 52))
    flag_large.save(str(base_path)+'/gfx/flags/'+tag_input+'.tga')
    flag_medium = flag_orig.resize((41, 26))
    flag_medium.save(str(base_path)+'/gfx/flags/medium/'+tag_input+'.tga')
    flag_small = flag_orig.resize((10, 7))
    flag_small.save(str(base_path)+'/gfx/flags/small/'+tag_input+'.tga')




