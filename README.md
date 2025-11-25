# MealMaster – Recipe & Meal Planning App

CSC 317 – Foundations of Software Development  
Fall 2025  
Team Coding Crew  
- Kimberlee Short – Project Manager / Database & Server Developer  
- James Ainsworth – Backend Designer  
- Patricia Cole – Frontend / UI Developer  
- Dipraj Shah – Quality Assurance Tester  

---

## Overview

**MealMaster** is a Python + Kivy application that helps users organize recipes and plan meals more easily.  
The app allows users to log in, view a dashboard, browse recipes, track pantry ingredients, and adjust basic settings.

This repository contains the full source code and supporting files for our final project deliverable for **Milestone 3**.

---

## Features

- **Login / Create Account** – Entry point for users to access their MealMaster workspace.  
- **Dashboard** – Central hub that links to Recipes, Pantry, and Settings pages.  
- **Recipes Page** – Displays saved recipes and basic details.  
- **Pantry Page** – Tracks ingredients on hand to support meal planning.  
- **Settings Page** – Allows the user to adjust simple application preferences.  

(See the included design and test documents in the `docs/` folder for more detail on UI flow and requirements coverage.)

---

## Project Structure

```text
MealMaster/
├── MealMaster.py           # Main application entry point
├── MealMasterLayout.kv     # Kivy layout describing GUI screens
├── backend/                # Backend logic, data, and database-related code
└── docs/                   # Design and test documentation (GUI design, QA plan, etc.)
