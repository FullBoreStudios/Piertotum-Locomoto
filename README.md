# Piertotum-Locomoto

Piertotum-Locomoto is a hardware and software project that enables custom interactions using a wand or device with an IR led point or reflector.

We are using a webcam with its IR filter removed and replaced with a piece of exposed film to filter out all other light spectrums.

## Example

![Piertotum-Locomoto in action](urawizzzzard.gif)

## Next Steps

Our goal is to see if we can get Piertotum-Locomoto to trigger spells in the new Hogwarts Legacy game. We are also planning to enable a few things at the Pennington Station, such as interactions using Arduino, motors, sounds, and other devices.

## Forking and Contributing

Feel free to suggest improvements to the project. We are planning to evolve this project to work more like an API, which may include a Flask set up so networked devices can be triggered.

Here are some next steps for the project:

1. Piertotum-Locomoto should be able to run on any low-power Windows, Linux, or Raspberry Pi computer with a webcam hooked up (with no IR filter and a polarizing light filter/film).

2. We need to have a dashboard to add spell configurations and configure endpoints.

3. Endpoints should be able to poll or receive input from anything on the network running Piertotum-Locomoto detection piece and then run whatever code they need to activate an interaction.
