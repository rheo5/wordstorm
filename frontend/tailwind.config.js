const { publicDecrypt } = require("crypto");
const { scryRenderedComponentsWithType } = require("react-dom/test-utils");

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx,html,css}"],
  theme: {
    extend: {},
  },
  plugins: [],
};
