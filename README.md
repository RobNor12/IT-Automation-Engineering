# Credential Generator & Lifecycle Manager

## Overview
The **Credential Generator** is a secure, command-line administrative utility designed to reduce the manual labor and human error involved in producing and decommissioning standardized credentials for an organization. It enforces strict naming conventions, validates administrative permissions, and manages credential persistence cleanly through local data structures.

## Technology Used
* **Python** (Core scripting, input validation, and logic flow)
* **Pandas** (Data manipulation and clean CSV persistence)
* **OS / Sys / Random** (File safety checks, system exit handling, and secure ID generation)

## Key Features
* **Secure Authentication (`auth`)**: Validates administrative access against a localized credential tracking file and implements a compromise-detection check if multiple unexpected password entries are found.
* **Standardized Generation (`gen_credentials`)**: Prompts administrators for names, enforces strict character limits (3–15 characters), extracts initials, and appends a cryptographically randomized 9-digit suffix separated by an underscore (e.g., `rlm_123456789`).
* **Interactive Decommissioning (`remove_credentials`)**: Allows administrators to review existing credentials individually, decide whether to purge or keep them, and gracefully exit or save changes at any point.
* **Robust Input Validation**: Implements strict validation loops on all user prompts to catch unexpected inputs and guide administrators safely.

## How to Use

* **1.** install requirments.txt 
