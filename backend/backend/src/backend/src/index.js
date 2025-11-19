import express from "express";
import dotenv from "dotenv";
import { pool } from "./db.js";

dotenv.config();
const app = express();
app.use(express.json());

app.get("/health", (req, res) => {
  res.json({ ok: true });
});

// sample route to test DB
app.get("/recipes", async (req, res) => {
  const result = await pool.query("SELECT * FROM recipes");
  res.json(result.rows);
});

const port = process.env.PORT || 3000;
app.listen(port, () =>
  console.log(`Server running on http://localhost:${port}`)
);
