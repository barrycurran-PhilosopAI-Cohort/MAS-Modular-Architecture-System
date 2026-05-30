# README.md

# CEPHALOPODAI | Intelligent Design | LLM Interface System
### Local Intelligence Workspace Terminal — Release V2.0

Academic Research: This project is built on the research paper: CephalopodAI: Universal Cognitive Sovereignty, Architecting Cloud-Free, Sovereign Intelligence for Professional Ethics and Personal Privacy (SSRN ID: 6850280).


PROJECT VISION & SYSTEMS PHILOSOPHY 


Welcome to CephalopodAI, a self-contained, stateless, edge-optimized terminal, an Agentic GUI, designed to serve as a highly collaborative local writing and engineering workbench. This system bridges the architectural gap between local large language models (LLMs), real-time external data retrieval, and active workspace rendering.

By fusing the local execution power of Ollama with the optimized weights of 
the Gemma 4:e2b model and our decoupled backend routing layer, this framework 
enables a heavyweight, highly intelligent local pipeline on your consumer 
hardware—operating flawlessly with or without an internet connection.  

This platform is engineered on a foundational principle of absolute 
Intellectual Sovereignty: your machine, your data, your rules. Unlike cloud-
hosted AI services that harvest usage telemetry and user inputs, CephalopodAI 
is a 100% locally-contained workspace. This ensures that your private 
manuscripts, academic research papers, proprietary source code, and strategic 
frameworks remain permanently shielded from external data harvesting, 
surveillance, or unauthorized access.  

Our mission is to freely distribute this operational capability to the world. 
The architecture is decoupled from corporate API paywalls and high-end 
enterprise server requirements, rendering it universally accessible. Whether 
you are a legal professional requiring air-gapped data confidentiality, or an 
independent builder cobbling an AI workstation together from spare parts, 
CephalopodAI delivers professional-grade computational intelligence directly 
to your desktop.  

================================================================================
2. REPOSITORY FILE MANIFEST
================================================================================

This repository contains the following core files. Ensure all background 
scripts and interfaces are kept in their matching directories to preserve 
relative cross-panel path routing:

* CEPHALOPODAI  Intelligent Design  LLM Interface3.docx
  - The complete v12 master system reference manual.  

* SYSTEM_SETUP_AND_INSTALLATION_GUIDE.docx
  - The foundational deployment and hardware verification handbook.  

* CEPHALOPODAI  Intelligent Design  LLM Interface3.txt
  - Plaintext backup of the technical user manual for terminal reference.

* README.MD
  - This primary portal documentation file.

* CEPHLOPODAI_INTERFACE_Itellectual_Freedom_V2.0.html
  - The core frontend application. A hardware-efficient, sleek, true 
    AMOLED pitch-black control room window.  

* Package.json
  - Manifest file establishing dependencies and configuring modern ES 
    module syntax handling.  

* Toolserver.js
  - The backend tool utility engine managing local web scraping, network 
    sifting, and live data lookup injections.  

================================================================================
3. CORE HARDWARE VERIFICATION
================================================================================

To run local inference via the Gemma 4:e2b engine without system latency loops 
or bottlenecks, verify your machine meets or exceeds these verified parameters:  

* Processor (CPU): Intel Core i5-10600K @ 4.10 GHz (or multi-core equivalent).  
* System Memory (RAM): 32 GB DDR4 @ 3000 MT/s.  
* Graphics Card (GPU): NVIDIA GeForce GTX 1080 Ti with 11 GB VRAM (Critical).  
* Storage Space: Solid State Drive (SSD) with 20 GB to 30 GB of free space.  
* Operating System (OS): Microsoft Windows 10 or Windows 11 (64-bit Architecture).  

[Hardware Note]: 11 GB of VRAM is required to load the full weights matrix of 
the model directly into high-speed GPU cache, guaranteeing instant execution 
and preventing lockups during massive sessions.  

================================================================================
4. QUICK-START INSTALLATION GUIDE
================================================================================

--------------------------------------------------------------------------------
Step 1: Initialize the Ollama Engine
--------------------------------------------------------------------------------
1. Go online and download the setup bundle from https://ollama.com/.  
2. Run OllamaSetup.exe and complete the on-screen installer prompts.  
3. Verify the Llama background icon is active within your Windows taskbar tray.  
4. Open your Command Prompt (cmd) and pull down the model weights by executing 
   the following command exactly:  

   ollama run gemma4:e2b

5. Once the download progress finishes, type /exit and hit Enter to close the 
   active model prompt loop.  

--------------------------------------------------------------------------------
Step 2: Establish the Node.js Runtime
--------------------------------------------------------------------------------
1. Navigate to https://nodejs.org/ and download the LTS (Long Term Support) 
   version installer.  
2. Run the installer, accept the terms, and check the box to install tools 
   for native modules before clicking Finish.  
3. Open a fresh Command Prompt window (cmd) and verify your system execution 
   paths by typing: 
   node -v
   npm -v

--------------------------------------------------------------------------------
Step 3: Assemble the Local Workspace
--------------------------------------------------------------------------------
1. Create a folder named lowercase "toolserver" on your Windows Desktop.  
2. Place your package.json and toolserver.js files directly inside that 
   directory path (e.g., C:\Users\YOUR_NAME\Desktop\toolserver).  
3. Open a Command Prompt, navigate to the folder where you placed the files, 
   and install the network scraping dependencies by running these lines:  

   cd C:\Users\YOUR_NAME\Desktop\toolserver
   npm install

(Note: Replace "YOUR_NAME" in the command above with your actual Windows username, 
or navigate to your specific folder path.)

--------------------------------------------------------------------------------
Step 4: System Execution Sequence
--------------------------------------------------------------------------------

[Launch Backend]: 
In your open terminal directory, execute the background bridge tool:  

   node toolserver.js

Confirm that the prompt returns: "Server Active on 3001". Minimize this 
command window; do not close it.  

[Launch Frontend]: 
Go to your repository folder, right-click the file named 
CEPHLOPODAI_INTERFACE_Itellectual_Freedom_V2.0.html, select "Open With", 
and choose Google Chrome or Microsoft Edge.  

================================================================================
5. COMPLETE WORKSPACE MASTER GUIDE
================================================================================

The interface divides operational labor into three distinct zones to maintain 
non-linear text creation workflows without losing data focus:  

+----------------------------------------------------------------------------+
|             STATUS BAR: Live Time & Cumulative Token Diagnostics           |
+----------------------------------------------------------------------------+
|  LEFT PANEL: PIPELINE CORE     |  RIGHT PANEL: PERSISTENT WORKSPACE        |
|                                |                                           |
|  [Active Chat Log Terminal]    |  [The Canvas Workspace Area]              |
|  - Displays chron streams.     |  - 100% independent text scratchpad.      |
|                                |  - Keeps core documents from scrolling    |
|  [Prompt Input Textarea]       |    away or burying under logs.            |
|  - Draft instructions/queries. |                                           |
|                                |  [Canvas Controls]                        |
|  [Live Code Sandbox]           |  - Save Canvas (UNIVERSAL .MD EXPORT)     |
|  - Green-on-black layout.      |  - Send Canvas to Prompt Bridge           |
|  - Run HTML/CSS/JS instantly.  |                                           |
+----------------------------------------------------------------------------+

--------------------------------------------------------------------------------
A. The Core Interaction Methods
--------------------------------------------------------------------------------
* The Basic Transmit Loop: 
  Type your research instructions or text modifications into the Prompt Input 
  and hit Transmit. This routes your prompt along with the entire cached 
  messageHistory array back to the local engine, appending answers cleanly 
  to your screen with automated layout tracking.  

* Live Net Search Lookups: 
  Type a search query and click Net Search. The backend toolserver.js grabs 
  the external query HTML, strips junk structural tracking tags using regex 
  sifters, and injects clean text blocks directly into the model's chat log 
  as system_data for immediate contextual analysis.  

--------------------------------------------------------------------------------
B. The Cross-Panel Telemetry Bridge
--------------------------------------------------------------------------------
* Send to Canvas: 
  Located below incoming responses in the chat log. Clicking it instantly 
  clones the text over to the right-hand Canvas workspace. It automatically 
  splits blocks with a secure, permanent "--- Response Capture ---" 
  timestamp string, logging exactly when information was synthesized.  

* Send Canvas to Prompt: 
  Clicking this clones your entire long-form manuscript or codebase from 
  the right canvas directly back into the left input prompt field. This 
  allows you to immediately instruct the AI to refine, expand, debug, or 
  rewrite extensive documents without manually selecting or cutting text.  

--------------------------------------------------------------------------------
C. Cognitive State Management
--------------------------------------------------------------------------------
* Save Session: 
  Compiles your active session title, exact time markers, total token metrics, 
  and the absolute chronological messageHistory into a portable .json file. 
  This acts as a portable "state cartridge".  

* Load Session: 
  Wipes the existing window and reloads a saved .json cartridge file. This 
  clears the view and resets the model’s active working memory cache, 
  protecting you from text drift and allowing you to instantly hop between 
  unrelated projects (e.g., swapping from data analysis code straight into 
  creative fiction writing).  

--------------------------------------------------------------------------------
D. Multi-Modal Ingestion & Local Sandbox
--------------------------------------------------------------------------------
* Direct File Dropping: 
  Drag and drop .txt, .md, or .json files straight into the workspace to 
  render them instantly. Dropping .docx files activates the integrated 
  Mammoth.js tool to strip away proprietary styles and extract raw text 
  natively into your panels.  

* The Sandbox Runner: 
  Paste HTML, CSS, or JavaScript blocks into the execution bay and click 
  Run Code. It builds and fires prototypes instantly inside an isolated 
  browser environment, making it perfect for rapid prototyping without 
  affecting your system's security layers.  

================================================================================
6. REPOSITORY LICENSING MATRIX
================================================================================

This repository is protected and governed by the Sovereign Commons Public 
License (SCPL Version 1.0), combining the structural rules of CC BY-NC-SA 4.0 
with specific user addendums:

* Individual, Academic, & Professional Freedom (PERMITTED): 
  Absolute permission is granted to any individual, researcher, hobbyist, 
  small business entity, or private professional (lawyers, doctors, writers, 
  engineers) to run, execute, modify, and utilize this tool locally for 
  internal productivity, daily business workflows, and private research. 
  Using this tool to help perform your daily work is 100% authorized, legal, 
  and encouraged.

* Corporate Exploitation Barrier (PROHIBITED): 
  Mega-corporations, corporate software conglomerates, and commercial software 
  distributors are strictly prohibited from commercializing this software core, 
  its unique layout design, or its twin-panel telemetry bridge. You cannot 
  sell copies of this software, bundle it into commercial application 
  packages, or integrate it into cloud-hosted, paid subscription Software-as-
  a-Service (SaaS) frameworks.

* Telemetry Enforcement: 
  Any attempt by a corporate entity to adapt or distribute this software for 
  the purpose of re-introducing centralized telemetry harvesting, user logging, 
  or data mining is a direct violation of this license.

For the unedited, full legal text and warranty disclaimers, review the master 
LICENSE.txt file located within the root directory of this repository.

--------------------------------------------------------------------------------
the architect
