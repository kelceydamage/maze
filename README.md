## Dev concepts

Interaction with the game world is only done via helpers. The main engine loads these helpers in order for engine functions to be able to interface with the world.

helpers include
* helpers.geographer
* helpers.cartographer
* helpers.calligrapher
* helpers.horticulturist
* helpers.biologist
* helpers.chronologist

### Geographer
Responsible for the manipulation of regions and terrain atrributes.

### Cartographer
Responsible for the manipulation of the overall map and region locations.

### Calligrapher
Responsible for organizing text objects for rendering.

### Horticulturist
Responsible for growth and change in the plants and vegetaion of the world.

### Biologist
Responsible for creating and revoking life in the world.

### Chronologist
Responsible for the sequencing of time and tracking dates.