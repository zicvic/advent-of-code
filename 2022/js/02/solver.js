import fs from "fs/promises";

const WEAPONS = ["A", "B", "C"];
const STRATEGIES = ["X", "Y", "Z"];

const SCORE = {
  win: 6,
  draw: 3,
  loss: 0,
};

async function readColumns(fileName) {
  const file = await fs.readFile(fileName, "utf8");
  const arr = file.split(/\r?\n/);
  return arr.map((i) => i.split(/\s/));
}

const getChoiceFromStupidStrategy = (opponent, strat) => {
  return WEAPONS[STRATEGIES.indexOf(strat)];
};

const getChoiceFromStrategy = (opponent, strat) => {
  const oIndex = WEAPONS.indexOf(opponent);
  const sIndex = STRATEGIES.indexOf(strat);
  let choice;
  if (sIndex === 1) {
    choice = oIndex;
  } else {
    choice = sIndex === 2 ? (oIndex + 1) % 3 : (oIndex + 2) % 3;
  }
  return WEAPONS[choice];
};

const rockPaperScissors = (opponent, you, strategyFunction) => {
  const oIndex = WEAPONS.indexOf(opponent);
  const uIndex = WEAPONS.indexOf(strategyFunction(opponent, you));
  let score;
  if (oIndex !== uIndex) {
    score = oIndex === (uIndex + 1) % 3 ? SCORE.loss : SCORE.win;
  } else {
    score = SCORE.draw;
  }
  return score + uIndex + 1;
};

const data1 = await readColumns("input-1.txt");
const data2 = await readColumns("input-2.txt");

const scorePart1 = data1
  .map((fight) => rockPaperScissors(...fight, getChoiceFromStupidStrategy))
  .reduce((acc, curr) => acc + curr, 0);

console.log(`Score Part 1: ${scorePart1}`);

const scorePart2 = data2
  .map((fight) => rockPaperScissors(...fight, getChoiceFromStrategy))
  .reduce((acc, curr) => acc + curr, 0);

console.log(`Score Part 2: ${scorePart2}`);
