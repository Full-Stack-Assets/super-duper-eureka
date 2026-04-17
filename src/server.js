import express from "express";
import fs from "node:fs";
import path from "node:path";

const app = express();
const staticPath = process.env.STATIC_PATH
  ? path.resolve(process.cwd(), process.env.STATIC_PATH)
  : path.resolve(process.cwd(), "dist", "public");
const indexFilePath = path.join(staticPath, "index.html");
const indexHtml = fs.existsSync(indexFilePath) ? fs.readFileSync(indexFilePath, "utf8") : null;

app.use(express.static(staticPath));

app.get("*", (_req, res) => {
  if (!indexHtml) {
    res.status(503).json({ error: "Static bundle is unavailable." });
    return;
  }

  res.type("html").send(indexHtml);
});

export default app;
