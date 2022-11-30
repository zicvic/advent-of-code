import fs from "fs/promises";

async function readArr(fileName) {
  const data = await fs.readFile(fileName, "utf8");
  const arr = data.split(/\r?\n/);
  return arr.map((i) => Number(i));
}

const data1 = await readArr("input-1.txt");

function solver(data) {
  return data.filter((a, i) => {
    if (i > 0) {
      return a > data[i - 1];
    } else {
      false;
    }
  });
}

const data2 = await readArr("input-2.txt");
const tripples = [];
for (let i = 0; i < data2.length - 2; i++) {
  tripples.push(data2[i] + data2[i + 1] + data2[i + 2]);
}

console.log(`The answer part 1 is: ${solver(data1).length}`);
console.log(`The answer part 2 is: ${solver(tripples).length}`);
