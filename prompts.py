import os
def identifier_subject(subject_name):
    # This function takes the subject name used in diffusekrona and return unique identifier of that subject.
    subject_class_dict = {
        'backpack': 'sksbackpack,backpack',
        'backpack_dog': 'sksbackpack_dog,backpack',
        'bear_plushie': 'sksbear_plushie,stuffed animal',
        'berry_bowl': 'sksberry_bowl,bowl',
        'can': 'skscan,can',
        'car2':'skscar2,car',
        'candle': 'skscandle,candle',
        'cat': 'skscat,cat',
        'cat2': 'skscat2,cat',
        'clock': 'sksclock,clock',
        'colorful_sneaker': 'skscolorful_sneaker,sneaker',
        'dog': 'sksdog,dog',
        'dog2': 'sksdog2,dog',
        'dog3': 'sksdog3,dog',
        'dog5': 'sksdog5,dog',
        'dog6': 'sksdog6,dog',
        'dog7': 'sksdog7,dog',
        'dog8': 'sksdog8,dog',
        'duck_toy': 'sksduck_toy,toy',
        'fancy_boot': 'sksfancy_boot,boot',
        'grey_sloth_plushie': 'sksgrey_sloth_plushie,stuffed animal',
        'monster_toy': 'sksmonster_toy,toy',
        'pink_sunglasses': 'skspink_sunglasses,sunglasses',
        'poop_emoji': 'skspoop_emoji,toy',
        'rc_car': 'sksrc_car,toy',
        'red_cartoon': 'sksred_cartoon,cartoon',
        'robot_toy': 'sksrobot_toy,toy',
        'shiny_sneaker': 'sksshiny_sneaker,sneaker',
        'teapot': 'sksteapot,teapot',
        'vase': 'sksvase,vase',
        'wolf_plushie': 'skswolf_plushie,stuffed animal',
        'face' : 'sksface',
        'takadaakemi':'skstakada,akemi',
        'supersaiyan':'skssupersaiyan,saiyan',
        'pokemon':'skspokemon',
        'kiriko':'skskiriko'
    }
    return subject_class_dict[subject_name]
 

def get_promts(subject_name):
    # This function takes the subject name used in diffusekrona and return prompts used in inference evaluation.
    livig_dataset=["cat","cat2","dog","dog2","dog3","dog5","dog6","dog7","dog8"]
    non_living_dataset= ['backpack','backpack_dog','bear_plushie','berry_bowl','can','candle' ,'clock' ,'colorful_sneaker','duck_toy','fancy_boot','grey_sloth_plushie','monster_toy','pink_sunglasses','poop_emoji','rc_car','red_cartoon','robot_toy','shiny_sneaker','teapot','vase','wolf_plushie']
    unique_token = subject_name
    class_token = identifier_subject(subject_name)
    add_ones=[]
    if unique_token=="teapot":
        add_ones=[
            "A {V} teapot floating in milk",
            "A transparent {V} teapot with milk inside",
            "A {V} teapot pouring tea",
            "A {V} teapot floating in the sea",
            "A bear pouring from a {V} teapot"
        ]
        add_ones = [sentence.format(V=unique_token) for sentence in add_ones]

    elif unique_token=="clock":
        add_ones = [
            'a {0} clock with a cave in the background'.format(unique_token),
            'A {0} clock on top of blue fabric'.format(unique_token),
            'A {0} clock held by a hand, with a forest in the background'.format(unique_token)
        ]

    elif unique_token=="dog6":
        add_ones = [
            'a {0} dog in a swimming pool'.format(unique_token),
            'a {0} dog in the Acropolis'.format(unique_token),
            'a {0} dog in a doghouse'.format(unique_token),
            'a {0} dog in a bucket'.format(unique_token),
            'a {0} dog getting a haircut'.format(unique_token),
            'a depressed {0} dog'.format(unique_token),
            'a sleeping {0} dog'.format(unique_token),
            'a sad {0} dog'.format(unique_token),
            'a joyous {0} dog'.format(unique_token),
            'a barking {0} dog'.format(unique_token),
            'a crying {0} dog'.format(unique_token),
            'a frowning {0} dog'.format(unique_token),
            'a screaming {0} dog'.format(unique_token)
        ]

    elif unique_token == "vase":
        add_ones = [
            'a {0} vase in the Acropolis'.format(unique_token),
            'A {0} vase in the ocean'.format(unique_token),
            'A {0} vase with a colorful flower bouquet'.format(unique_token),
            'Milk poured into a {0} vase'.format(unique_token),
            'A {0} vase buried in the sands'.format(unique_token),
            'Two {0} vases on a table'.format(unique_token)
        ]
        
    elif unique_token == "cat":
        add_ones = [
            'a {0} cat seen from the top'.format(unique_token),
            'a {0} cat seen from the bottom'.format(unique_token),
            'a {0} cat seen from the side'.format(unique_token),
            'a {0} cat seen from the back'.format(unique_token)
        ]

    elif unique_token == "dog2":
        add_ones = [
            'a {0} dog wearing a witch outfit'.format(unique_token),
            'a {0} dog wearing Angel Wings'.format(unique_token),
            'a {0} dog wearing a Superman Outfit'.format(unique_token),
            'a {0} dog wearing an Ironman Outfit'.format(unique_token),
            'a {0} dog wearing a Nurse Outfit'.format(unique_token),
            'A cross of a {0} dog and a bear'.format(unique_token),
            'A cross of a {0} dog and a panda'.format(unique_token),
            'A cross of a {0} dog and a koala'.format(unique_token),
            'A cross of a {0} dog and a lion'.format(unique_token),
            'A cross of a {0} dog and a hippo'.format(unique_token)
        ]

    
    elif unique_token == "backpack":
        add_ones = [
            'A {0} backpack in the Grand Canyon'.format(unique_token),
            'A wet {0} backpack in water'.format(unique_token),
            'A {0} backpack in Boston'.format(unique_token),
            'A {0} backpack with the night sky'.format(unique_token)
        ]

    elif unique_token == "pink_sunglasses":
        add_ones = [
            'A {0} sunglasses in the jungle'.format(unique_token),
            'A {0} sunglasses worn by a bear'.format(unique_token),
            'A {0} sunglasses at Mt. Fuji'.format(unique_token),
            'A {0} sunglasses with the Eiffel Tower in the background'.format(unique_token)
        ]

    elif unique_token == "dog":
        add_ones = [
            'A {0} dog in the Versailles Hall of Mirrors'.format(unique_token),
            'A {0} dog in the gardens of Versailles'.format(unique_token),
            'A {0} dog in Coachella'.format(unique_token),
            'A {0} dog in Mount Fuji'.format(unique_token),
            'A {0} dog with the Eiffel Tower in the background'.format(unique_token)
        ]


    elif unique_token == "dog5":
        add_ones = [
            'a {0} dog image in the form of Vincent Van Gogh painting'.format(unique_token),
            'a {0} dog image in the form of Michelangelo painting'.format(unique_token),
            'a {0} dog image in the form of Rembrandt painting'.format(unique_token),
            'a {0} dog image in the form of Leonardo da Vinci painting'.format(unique_token),
            'a {0} dog image in the form of Pierre-Auguste Renoir painting'.format(unique_token),
            'a {0} dog image in the form of Johannes Vermeer painting'.format(unique_token)
        ]

    
    elif unique_token == "car2":
        add_ones = [
            'A red {0} car'.format(unique_token),
            'A purple {0} car'.format(unique_token),
            'A pink {0} car'.format(unique_token),
            'A blue {0} car'.format(unique_token),
            'A yellow {0} car'.format(unique_token)
        ]
    
    else:
        add_ones = []

    if unique_token in non_living_dataset :
        object_prompt_list = ['a {0} {1} in the jungle'.format(unique_token, class_token),
            'a {0} {1} in the snow'.format(unique_token, class_token),
            'a {0} {1} on the beach'.format(unique_token, class_token),
            'a {0} {1} on a cobblestone street'.format(unique_token, class_token),
            'a {0} {1} on top of pink fabric'.format(unique_token, class_token),
            'a {0} {1} on top of a wooden floor'.format(unique_token, class_token),
            'a {0} {1} with a city in the background'.format(unique_token, class_token),
            'a {0} {1} with a mountain in the background'.format(unique_token, class_token),
            'a {0} {1} with a blue house in the background'.format(unique_token, class_token),
            'a {0} {1} on top of a purple rug in a forest'.format(unique_token, class_token),
            'a {0} {1} with a wheat field in the background'.format(unique_token, class_token),
            'a {0} {1} with a tree and autumn leaves in the background'.format(unique_token, class_token),
            'a {0} {1} with the Eiffel Tower in the background'.format(unique_token, class_token),
            'a {0} {1} floating on top of water'.format(unique_token, class_token),
            'a {0} {1} floating in an ocean of milk'.format(unique_token, class_token),
            'a {0} {1} on top of green grass with sunflowers around it'.format(unique_token, class_token),
            'a {0} {1} on top of a mirror'.format(unique_token, class_token),
            'a {0} {1} on top of the sidewalk in a crowded street'.format(unique_token, class_token),
            'a {0} {1} on top of a dirt road'.format(unique_token, class_token),
            'a {0} {1} on top of a white rug'.format(unique_token, class_token),
            'a red {0} {1}'.format(unique_token, class_token),
            'a purple {0} {1}'.format(unique_token, class_token),
            'a shiny {0} {1}'.format(unique_token, class_token),
            'a wet {0} {1}'.format(unique_token, class_token),
            'a cube shaped {0} {1}'.format(unique_token, class_token)
        ]
        if len(add_ones) > 0:
            return add_ones + object_prompt_list
        return object_prompt_list

    if(unique_token in livig_dataset):
        live_prompt_list = ['a {0} {1} in the jungle'.format(unique_token, class_token),
            'a {0} {1} in the snow'.format(unique_token, class_token),
            'a {0} {1} on the beach'.format(unique_token, class_token),
            'a {0} {1} on a cobblestone street'.format(unique_token, class_token),
            'a {0} {1} on top of pink fabric'.format(unique_token, class_token),
            'a {0} {1} on top of a wooden floor'.format(unique_token, class_token),
            'a {0} {1} with a city in the background'.format(unique_token, class_token),
            'a {0} {1} with a mountain in the background'.format(unique_token, class_token),
            'a {0} {1} with a blue house in the background'.format(unique_token, class_token),
            'a {0} {1} on top of a purple rug in a forest'.format(unique_token, class_token),
            'a {0} {1} wearing a red hat'.format(unique_token, class_token),
            'a {0} {1} wearing a santa hat'.format(unique_token, class_token),
            'a {0} {1} wearing a rainbow scarf'.format(unique_token, class_token),
            'a {0} {1} wearing a black top hat and a monocle'.format(unique_token, class_token),
            'a {0} {1} in a chef outfit'.format(unique_token, class_token),
            'a {0} {1} in a firefighter outfit'.format(unique_token, class_token),
            'a {0} {1} in a police outfit'.format(unique_token, class_token),
            'a {0} {1} wearing pink glasses'.format(unique_token, class_token),
            'a {0} {1} wearing a yellow shirt'.format(unique_token, class_token),
            'a {0} {1} in a purple wizard outfit'.format(unique_token, class_token),
            'a red {0} {1}'.format(unique_token, class_token),
            'a purple {0} {1}'.format(unique_token, class_token),
            'a shiny {0} {1}'.format(unique_token, class_token),
            'a wet {0} {1}'.format(unique_token, class_token),
            'a cube shaped {0} {1}'.format(unique_token, class_token)
        ]
        if len(add_ones) > 0:
            return add_ones + live_prompt_list
        return live_prompt_list
    
    if(unique_token == "face"):
        face_prompts = [""]
        return face_prompts
    
    if(unique_token == "pokemon"):
        from datasets import load_dataset
        ds = load_dataset("lambdalabs/pokemon-blip-captions", split="train")
        text_array = []  # Array to store the "text" values
        for i in range(len(ds)):
            sample = ds[i]
            text_array.append("A pokemon with" + sample["text"])
        return text_array
    
    if(unique_token == "kiriko"):
        prompts = ["Kiriko, a fierce warrior with a flaming sword.",
            "Stealthy Kiriko, armed with deadly daggers.",
            "Mysterious sorceress Kiriko with silver hair.",
            "Golden-haired Kiriko, an unparalleled archer.",
            "Mischievous jester Kiriko with purple hair.",
            "Noble knight Kiriko in intricate armor.",
            "Inventor Kiriko with wild hair and goggles.",
            "Elegant dancer Kiriko in a shimmering dress.",
            "Kiriko, a swift and nimble thief.",
            "Kiriko, a stoic and disciplined samurai.",
            "Kiriko, a wise and ancient druid.",
            "Kiriko, a charismatic pirate captain.",
            "Kiriko, a master of elemental magic.",
            "Kiriko, a skilled martial artist with lightning-fast strikes.",
            "Kiriko, a fearless monster hunter.",
            "Kiriko, a cunning spy skilled in espionage.",
            "Kiriko, a vengeful avenger with a dark past.",
            "Kiriko, a guardian of sacred artifacts.",
            "Kiriko, a celestial being with angelic wings.",
            "Kiriko, a mechanical genius who constructs robotic companions.",
            "Kiriko, a cursed vampire seeking redemption.",
            "Kiriko, a tribal warrior adorned with tribal tattoos.",
            "Kiriko, a time traveler armed with advanced technology.",
            "Kiriko, a master of illusions and mind manipulation.",
            "Kiriko, a master archer who never misses her mark.",
            "Kiriko, a cyborg warrior with augmented strength.",
            "Kiriko, a mystical shaman with a connection to nature.",
            "Kiriko, a master tactician and strategic genius.",
            "Kiriko, a fearless gladiator in an arena of death.",
            "Kiriko, a celestial being with wings of shadow.",
            "Kiriko, a guardian of ancient ruins and secrets.",
            "Kiriko, a skilled alchemist brewing powerful potions.",
            "Kiriko, a quick-witted rogue and master of disguise.",
            "Kiriko, a haunted soul seeking redemption.",
            "Kiriko, a tribal huntress with a bond with animals.",
            "Kiriko, a cyberspace hacker navigating virtual worlds.",
            "Kiriko, a cursed knight with a sentient sword.",
            "Kiriko, a ghostly apparition haunting the living.",
            "Kiriko, a mystical oracle with the gift of foresight.",
            "Kiriko, a deadly assassin lurking in the shadows.",
            "Kiriko, a martial arts prodigy with lightning reflexes.",
            "Kiriko, a legendary pirate queen commanding a fleet.",
            "Kiriko, a fallen angel seeking to reclaim her wings.",
            "Kiriko, a vengeful spirit with control over fire.",
            "Kiriko, a skilled hunter tracking down mythical creatures.",
            "Kiriko, a master of telekinesis and mind control.",
            "Kiriko, a samurai with a cursed, sentient katana.",
            "Kiriko, a master of ancient runes and magical symbols.",
            "Kiriko, a charming bard with a mesmerizing voice.",
            "Kiriko, a powerful sorceress harnessing the forces of nature."
        ]
        return prompts
    
    if(unique_token == "supersaiyan"):
        supersaiyan_prompts =["a photo of skssupersaiyan with spiky golden hair, glowing blue eyes, and a fierce expression.", #1
            "a photo of skssupersaiyan fusion between two characters, combining their physical features and unique traits, emanating a powerful aura.", #5
            "a photo of skssupersaiyan with emerald green hair, vibrant purple eyes, surrounded by swirling energy and cracks of lightning.", #6
            "a photo of skssupersaiyan surrounded by a halo of energy, creating shockwaves with every punch, in a destroyed cityscape.", #7
            "a photo of skssupersaiyan with wild, untamed red hair, wearing torn battle gi, charging a massive energy blast.", #8
            "a photo of skssupersaiyan with ice-blue hair and icy aura, depicted in a frozen tundra with floating ice shards.", #9
            "a photo of skssupersaiyan in an advanced transformation, with multiple energy auras emanating from their body, in a cosmic landscape.", #10
            "a photo of skssupersaiyan with golden hair that transitions into fiery red at the tips, engaged in a fierce battle, surrounded by rubble.", #11
            "a photo of skssupersaiyan with a dark, brooding appearance, jet-black hair, glowing red eyes, wielding a dark energy sword.", #12
            "a photo of skssupersaiyan with flowing silver hair and peaceful expression, meditating in a serene garden.", #13
            "a photo of skssupersaiyan with long, flowing hair changing colors from blue to purple in a gradient, charging a powerful energy beam.", #14
            "a photo of skssupersaiyan with golden hair that has a sparkling, starry effect, flying through the night sky, leaving trails of stardust.", #15
            "a photo of skssupersaiyan with fiery orange hair, intense gaze, surrounded by a tornado-like energy vortex.", #16
            "a photo of skssupersaiyan with jet-black hair, glowing silver eyes, training in a dark, otherworldly dimension.", #17
            "a photo of skssupersaiyan with vibrant, neon-colored hair, playful expression, riding on a hoverboard made of energy.", #18
            "a photo of skssupersaiyan in a berserker state, with wild, untamed hair, furious expression, unleashing devastating attacks.", #19
            "a photo of skssupersaiyan with transparent, crystalline hair that refracts light, surrounded by shards of energy crystals.", #20
            "a photo of skssupersaiyan with bioluminescent hair that glows in various shades of green, standing amidst a lush, vibrant forest.", #21
            "a photo of skssupersaiyan with ethereal, translucent hair resembling flowing water, surrounded by a misty, aquatic aura.", #22
            "a photo of skssupersaiyan with celestial-themed hair resembling swirling galaxies, floating in space, surrounded by nebulae and stars.", #23
            "a photo of skssupersaiyan with metallic silver hair, cybernetic augmentation on one arm, charging up an energy cannon.", #24
            "a photo of skssupersaiyan with fiery crimson hair, phoenix-like aura, soaring through the sky, leaving a trail of flames.", #25
            "a photo of skssupersaiyan with dual-colored hair split down the middle into contrasting shades, engaging in a high-speed aerial battle.", #26
            "a photo of skssupersaiyan with a wild, mane-like hairstyle made of golden lightning, unleashing a devastating lightning attack.", #27
            "a photo of skssupersaiyan with translucent, crystalline armor reflecting and refracting light, surrounded by an aura of energy constructs.", #28
            "a photo of skssupersaiyan with jet-black hair emitting a radiant, violet glow, standing atop a mountain peak, with a storm brewing in the background.", #29
            "a photo of skssupersaiyan with iridescent hair shifting in color depending on the angle, meditating under a waterfall.", #30
            "a photo of skssupersaiyan with bioluminescent tattoos glowing on their skin, summoning an enormous energy dragon.", #31
            "a photo of skssupersaiyan with transparent, crystalline wings shimmering with a rainbow of colors, flying through a serene, cloud-filled sky.", #32
            "a photo of skssupersaiyan with a partially transformed appearance, showcasing a mix of their normal form and Super Saiyan traits, training in a gravity chamber.", #33
            "a photo of skssupersaiyan with radiant, golden hair and angelic wings, healing a wounded ally with their energy.", #34
            "a photo of skssupersaiyan with a fiery aura engulfing their entire body, surrounded by crumbling rocks and lava.", #35
            "a photo of skssupersaiyan with a majestic, ethereal presence, emanating a soft, golden glow, wielding a staff made of pure energy.", #36
            "a photo of skssupersaiyan with crystalline armor and a helmet concealing their face, charging up a powerful energy sphere.", #37
            "a photo of skssupersaiyan with bioluminescent markings on their skin pulsing with energy, in deep focus, channeling their inner strength.", #38
            "a photo of skssupersaiyan with a shimmering, ethereal tail made of pure energy, engaged in a hand-to-hand combat stance.", #39
            "a photo of skssupersaiyan with multi-colored, flowing hair shifting hues dynamically, surrounded by a whirlwind of energy blades.", #40
            "a photo of skssupersaiyan with a sleek, streamlined appearance, wearing an advanced battle suit, charging up an energy beam from their palms.", #41
            "a photo of skssupersaiyan with fiery crimson hair, wearing a legendary golden armor, clashing swords with a formidable opponent.", #42
            "a photo of skssupersaiyan with luminescent, silver hair, standing atop a mountain peak, arms crossed, overlooking a vast landscape.", #43
            "a photo of skssupersaiyan with electrified, cobalt-blue hair, crackling with lightning, in mid-air, preparing to deliver a devastating punch.", #44
            "a photo of skssupersaiyan with a flowing mane of emerald green hair, surrounded by a cyclone of energy, unleashing a powerful ki blast.", #45
            "a photo of skssupersaiyan with radiant, golden hair and emerald-green eyes, emanating a calm and focused aura, meditating on a mountaintop.", #46
            "a photo of skssupersaiyan with flowing, pearl-white hair and a serene expression, standing on a serene beach, waves crashing behind them.", #47
            "a photo of skssupersaiyan with fiery, magma-red hair and magma-like energy aura, clenching their fists, ready for an intense battle.", #48
            "a photo of skssupersaiyan with violet-colored hair, wearing an elegant, flowing robe, surrounded by a serene garden filled with blooming flowers.", #49
            "a photo of skssupersaiyan with luminescent, golden hair, transcendent expression, and a halo of energy, radiating a divine power.", #50
        ]
        return supersaiyan_prompts
    
    if(unique_token == "takadaakemi"):
        prompts = ["image of skstakadaakemi, creamy mami, morisawa yuu, nega (creamy mami), posi (creamy mami), 1girl, ahoge, blue background, blue eyes, cat, choker, copyright name, dress, elbow gloves, flower, frills, gloves, hair flower, hair ornament, microphone, purple hair, short hair, smile, 1980s (style), painting (medium), retro artstyle, watercolor (medium)",
            "image of skstakadaakemi, creamy mami, morisawa yuu, 2girls, dress one wearing white other blue, hug, idol, magical girl, multiple girls, wings, 1980s (style), painting (medium), retro artstyle, watercolor (medium)",
            "image of skstakadaakemi, lucy (cyberpunk), 1girl, against railing, arm rest, bangs, bare shoulders, belt, black belt, black leotard, black pants, blurry, bob cut, breasts, building, cityscape, clothing cutout, cropped jacket, cyberpunk, depth of field, from side, gradient eyes, grey eyes, grey hair, holding, jacket, leotard, lips, long sleeves, looking afar, looking ahead, mechanical parts, medium breasts, multicolored eyes, multicolored hair, night, night sky, off shoulder, open clothes, open jacket, outdoors, pants, parted lips, railing, red eyeliner, science fiction, short hair with long locks, short shorts, shorts, sidelocks, sky, smoke, smoking, solo, standing, teeth, thigh cutout, upper teeth only, white jacket, white shorts, cyberpunk (series), cyberpunk edgerunners, 1980s (style), painting (medium), retro artstyle, watercolor (medium)",
            "image of skstakadaakemi, pyra (xenoblade), 1girl, armor, bangs, black gloves, breasts, red eyes, closed mouth, earrings, eyelashes, fingerless gloves, floating hair, framed breasts, gem, gloves, hair ornament, headpiece, jewelry, large breasts, leaning back, leotard, neon trim, official art, pose, red hair, red shorts, saitou masatsugu, short hair, short shorts, short sleeves, shorts, sidelocks, skin tight, solo, standing, swept bangs, thighhighs, tiara, space background, turtleneck, underbust, vambraces, xenoblade chronicles (series), (xenoblade chronicles 2), 1980s (style), painting (medium), retro artstyle, watercolor (medium)",
            "image of skstakadaakemi, (komi shouko), 1girl, bangs, blazer, blue jacket, blush, bow, bowtie, breasts, closed mouth, collared shirt, cowboy shot, expressionless, outdoors, highres, jacket, (komi-san wa komyushou desu), long hair, looking at viewer, medium breasts, purple eyes, purple hair, red bow, red bowtie school uniform, shirt, striped, striped bow, striped bowtie, striped skirt, swept bangs, white shirt, 1980s (style), painting (medium), retro artstyle, watercolor (medium)",
            "image of skstakadaakemi, creamy mami, morisawa yuu, nega (creamy mami), posi (creamy mami), 1girl, ahoge, blue background, blue eyes, cat, choker, copyright name,light purple-pink dress, elbow gloves, flower, frills, gloves, hair flower, hair ornament, microphone, purple hair, short hair, smile, 1980s (style), painting (medium), retro artstyle, watercolor (medium)",
            "image of skstakadaakemi, princess zelda, 1girl, bangs, blonde hair, breasts, bridal gauntlets, closed mouth, expressionless, from side, green eyes, highres, jewelry, long hair, long sleeves, nintendo, outdoors, pointy ears, ring, small breasts, solo, standing, the legend of zelda, tree, triforce print, upper body, blue shirt 1980s (style), painting (medium), retro artstyle, watercolor (medium)",
            "image of skstakadaakemi, yorha no. 2 type b, 1girl, black dress, black hairband, breasts, cleavage, black dress, hair over one eye, hairband, lips, long sleeves, looking at viewer, medium breasts, mole, mole under mouth, puffy long sleeves, puffy sleeves, short hair, signature, solo, white hair, blue eyes, outdoors, grass, trees, ruins, 1980s (style), painting (medium), retro artstyle, watercolor (medium)",
            "image of skstakadaakemi, eula (genshin impact), 1980s (style), 1girl, solo, mature female, mature, curvy, 1girl, solo, thighhighs, gloves, hairband, breasts, cape, bangs, thighs, leotard, necktie, light blue hair, blue hair, outdoors, long sleeves, looking at viewer, medium breasts, black gloves, blue necktie, hair ornament, black, black hairband, yellow eyes, closed mouth, blue cape, medium hair, arms above head, painting (medium), retro artstyle, traditional media, watercolor (medium)",
            "image of skstakadaakemi, mythra (xenoblade), 1girl, armor, bangs, bare shoulders, blonde hair, breasts, cleavage, closed mouth, dress, earrings, elbow gloves, eyelashes, floating hair, gem, gloves, hair ornament, hairband, headpiece, jewelry, large breasts, leaning back, long hair, neon trim, official art, pose, saitou masatsugu, sidelocks, skin tight, smile, solo, standing, swept bangs, tiara, space background, very long hair, white dress, xenoblade chronicles (series), (xenoblade chronicles 2), 1980s (style), painting (medium), retro artstyle, watercolor (medium)",
            "image of skstakadaakemi, creamy mami, morisawa yuu, 2girls, dress, hug, idol, magical girl, multiple girls, wings, black background like space 1980s (style), painting (medium), retro artstyle, watercolor (medium)",
            "image of skstakadaakemi, ((1boy)), bangs, black footwear, blue eyes, casual, dated, denim, headphones, hood, hood down, hoodie, jeans, long sleeves, looking at viewer, pants, red hair, short hair, sitting, solo, 1980s (style), painting (medium), retro artstyle, watercolor (medium)",
            "image of skstakadaakemi, white top black bottom dress, Tifa lockhart as magician, Final Fantasy VII, 1girl, small breast, beautiful eyes, brown hair, smiling, red eyes, highres, diamond earring, long hair,side parted hair, hair behind ear, upper body, stylish black dress, indoors, bar, 1980s (style), painting (medium), retro artstyle, watercolor (medium)",
            "image of skstakadaakemi, Tifa lockhart as magician, Final Fantasy VII, 1girl, small breast, beautiful eyes, brown hair, smiling, red eyes, highres, diamond earring, long hair, side parted hair, hair behind ear, upper body, stylish black dress, indoors, bar 1980s (style), painting (medium), retro artstyle, watercolor (medium)",
            "image of skstakadaakemi, Tifa lockhart as magician, Final Fantasy VII, 1girl, small breast, beautiful eyes, brown hair, smiling, red eyes, highres, diamond earring, long hair, side parted hair, hair behind ear, upper body, white sky blue stylish dress, indoors, bar, 1980s (style), painting (medium), retro artstyle, watercolor (medium)",
            "image of skstakadaakemi, Tifa lockhart as magician, Final Fantasy VII, 1girl, small breast, beautiful eyes, brown hair, smiling, red eyes, highres, diamond earring, long hair, side parted hair, hair behind ear, upper body, stylish purple-violet dress, indoors, bar, 1980s (style), painting (medium), retro artstyle, watercolor (medium), holding wine glass",
            "image of skstakadaakemi, painting (medium), retro artstyle, traditional media, watercolor (medium), 1980s (style), A beautiful woman, raw portrait, best quality, without makeup, lighting, highly detailed, outdoor, sleeveless white lace, freckle",
            "image of skstakadaakemi, painting (medium), retro artstyle, traditional media, watercolor (medium), 1980s (style), A beautiful girl, idol, pure face, best quality, raw portrait, highly detailed, skinny, supple and pale skin, sunlight, sleeveless, bow, tidy street",
            "image of skstakadaakemi, traditional media, 1980s (style), A beautiful woman, fantasy, nature, japan traditional dress, perfect face, masterpiece, best quality, lighting, highly detailed, body, balcony, sexy, trending on artstation",
            "image of skstakadaakemi, traditional media, 1980s (style), 1girl, masterpiece, best quality, fantasy uniform, crop top, kawaii, crystal gradient eyes, highly detailed, sunlight, indoors, colorful, white pink dress"
        ]
        return prompts
