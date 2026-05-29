import express from "express";
import cors from "cors";
import fetch from "node-fetch";

const app = express();
app.use(cors({ origin: "*" })); 
app.use(express.json());

app.post("/tool", async (req, res) => {
    const query = req.body.query;
    if (!query) return res.status(400).json({ error: "Missing query" });

    try {
        const url = `https://duckduckgo.com/html/?q=${encodeURIComponent(query)}`;
        const response = await fetch(url, {
            headers: { "User-Agent": "Mozilla/5.0" }
        });
        let html = await response.text();
        
        // 1. REGEX CLEANUP: Remove scripts, styles, and strip tags
        let cleanText = html
            .replace(/<script[^>]*>([\s\S]*?)<\/script>/gi, "")
            .replace(/<style[^>]*>([\s\S]*?)<\/style>/gi, "")
            .replace(/<[^>]+>/g, "\n");

        // 2. CONTENT SIFTER: Process line by line to keep only relevant info
        let lines = cleanText.split('\n');
        let filteredLines = lines.filter(line => {
            let trimmed = line.trim();
            // Keep the line ONLY if it's long enough to be a sentence AND has a period
            return trimmed.length > 30 && trimmed.includes('.');
        });

        // 3. COMBINE & PREPEND: Combine the sifted lines and add the header line
        let scrubbedData = filteredLines.join('\n\n');
        let finalResult = "Here are your search results:\n\n" + (scrubbedData || "No meaningful content could be extracted.");

        res.json({ result: finalResult });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

app.listen(3001, () => console.log("Server Active on 3001"));