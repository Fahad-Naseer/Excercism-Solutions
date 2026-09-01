export const EXPECTED_MINUTES_IN_OVEN = 40;

export function remainingMinutesInOven(actualMinutesInOven) {
  return EXPECTED_MINUTES_IN_OVEN - actualMinutesInOven;
}
remainingMinutesInOven(30);

export function preparationTimeInMinutes(numberOfLayers) {
  return numberOfLayers*2;
}
preparationTimeInMinutes(3);

export function totalTimeInMinutes(numberOfLayers, actualMinutesInOven) {
        return preparationTimeInMinutes(numberOfLayers)+ actualMinutesInOven;
}
totalTimeInMinutes(3,20);