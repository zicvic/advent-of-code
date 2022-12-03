import fs from "fs/promises";

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

const data = await readColumns("input-1.txt");

const rockPaperScissors = (opponent, you) => {
  const OPPONENT = ["A", "B", "C"];
  const YOU = ["X", "Y", "Z"];
  const oIndex = OPPONENT.indexOf(opponent);
  const uIndex = YOU.indexOf(you);
  let score;
  if (oIndex !== uIndex) {
    score = oIndex === (uIndex + 1) % 3 ? SCORE.loss : SCORE.win;
  } else {
    score = SCORE.draw;
  }
  return score + uIndex + 1;
};

const score = data
  .map((fight) => rockPaperScissors(...fight))
  .reduce((acc, curr) => acc + curr, 0);
console.log(score);
