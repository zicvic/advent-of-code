import fs from "fs/promises";

async function readArr(fileName) {
  const data = await fs.readFile(fileName, "utf8");
  const arr = data.split(/\r?\n/);
  return arr.map((i) => Number(i));
}

function calorieSum(data) {
  const sums = [];
  for (let i = 0; i < data.length; i++) {
    let elf = 0;
    while (data[i] > 0) {
      elf = elf + data[i];
      i++;
    }
    if (elf > 0) {
      sums.push(elf);
    }
  }
  return sums;
}

const data1 = await readArr("input1.txt");
const data2 = await readArr("input2.txt");

const elves2 = calorieSum(data2);

elves2.sort(function (a, b) {
  return a > b ? 1 : -1;
});

let top3 = 0;
for (let i = elves2.length - 1; i >= elves2.length - 3; i--) {
  top3 += elves2[i];
}

console.log(`The answer part 1 is: ${Math.max(...calorieSum(data1))}`);
console.log(`The answer part 2 is: ${top3}`);
