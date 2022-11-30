import fs from "fs/promises";

async function readArr(fileName) {
  const data = await fs.readFile(fileName, "utf8");
  const arr = data.split(/\r?\n/);
  return arr.map((i) => Number(i));
}

const data = await readArr("input.txt");

const answer = data.filter((a, i) => {
  if (i > 0) {
    return a > data[i - 1];
  } else {
    false;
  }
});

console.log(`The answer is: ${answer.length}`);
