import bpy
import math
import mathutils

# Clean the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Create the deck (75 cm x 45 cm x 10 cm) with rounded edges
bpy.ops.mesh.primitive_cube_add(size=1, location=(0.06, 0, -0.0225))
deck = bpy.context.object
deck.scale = (0.75 / 2, 0.45 / 2, 0.10 / 2)

# Apply smooth shading
bpy.ops.object.shade_smooth()

# Add a bevel modifier to round the edges
bpy.ops.object.modifier_add(type='BEVEL')
deck.modifiers["Bevel"].width = 0.9  # Adjust as needed
deck.modifiers["Bevel"].segments = 5

# Create the mast (1.2 m length with water-streamed profile)
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, -0.3525))  # Positioned below the deck
mast = bpy.context.object
mast.scale = (0.1, 0.015, 1.2 / 2)  # Thin in one direction, elongated in another


# Apply smooth shading
bpy.ops.object.shade_smooth()

# Create the mounting plate at the top of the mast
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, -0.05))  # Positioned on top of the mast
plate = bpy.context.object
plate.scale = (0.1, 0.1, 0.005)  # Thin plate

# Apply smooth shading
bpy.ops.object.shade_smooth()

# Create the fuselage (55 cm length, square profile 2 cm x 2 cm)
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, -0.6525))  # Positioned below the mast
fuselage = bpy.context.object
fuselage.scale = (0.55 / 2, 0.02, 0.02)

# Apply smooth shading
bpy.ops.object.shade_smooth()

# Create the front wing (90 cm x 15 cm x 3 cm)
bpy.ops.mesh.primitive_cube_add(size=1, location=(0.15, 0, -0.6525))  # Positioned in front of fuselage
front_wing = bpy.context.object
front_wing.scale = (0.15 / 2, 0.9 / 2, 0.03 / 2)

# Apply smooth shading
bpy.ops.object.shade_smooth()

# Add a subdivision surface modifier to make the wing aerodynamic
bpy.ops.object.modifier_add(type='SUBSURF')
front_wing.modifiers["Subdivision"].levels = 2
bpy.ops.object.modifier_apply(modifier="Subdivision")

# Create the stabilizer (12 cm x 6 cm x 1 cm)
bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.14, 0, -0.6525))  # Positioned behind fuselage
stabilizer = bpy.context.object
stabilizer.scale = (0.06 / 2, 0.24 / 2, 0.01 / 2)

# Apply smooth shading
bpy.ops.object.shade_smooth()

# Add a subdivision surface modifier to make the stabilizer aerodynamic
bpy.ops.object.modifier_add(type='SUBSURF')
stabilizer.modifiers["Subdivision"].levels = 2
bpy.ops.object.modifier_apply(modifier="Subdivision")

# Join all the objects into one solid construction
bpy.ops.object.select_all(action='DESELECT')
deck.select_set(True)
mast.select_set(True)
plate.select_set(True)
fuselage.select_set(True)
front_wing.select_set(True)
stabilizer.select_set(True)
bpy.context.view_layer.objects.active = deck
bpy.ops.object.join()

# Save the model as an STL file (optional)
# bpy.ops.export_mesh.stl(filepath="/path/to/save/untitle.stl")

