### **1. File: `statement.md`**

```markdown
# Problem Statement & System Scope

## Problem Statement
Traditional paper-based library management systems suffer from high tracking errors, manual search overhead, lost record entries, and inefficient inventory status updates. Existing software solutions often impose heavy hardware overhead or complex setup processes. There is a need for a lightweight, modular computational tool that provides immediate inventory state management, search capabilities, and analytics without heavy external dependencies.

## Scope of the Project
- **In-Scope:**
  - In-memory inventory management storing Book IDs, Titles, Prices, and Status flags.
  - Core CRUD-like operations: Viewing inventory, adding records, and issuing books.
  - Analytical features: Max-price record lookup and reverse sequence traversal.
  - Multi-module modular architecture (`main.py`, `data.py`, `view_books.py`, `issue.py`, `analytics.py`).
- **Out-of-Scope:**
  - Relational database management (SQLite/MySQL integration).
  - Web/Desktop Graphical User Interfaces (GUI).
  - External network deployment or multi-user network synchronization.

## Target Users
- **Academic Evaluators & Faculty:** Assessing software engineering practices, modular coding, and SDLC compliance for CSE1021.
- **Library Administrators / Librarians:** Managing small-scale catalog operations, checking status, and updating book issuance quickly via CLI.
- **Students & Programming Learners:** Reviewing clean multi-file Python architecture and basic array-based algorithms.

## High-Level Features
1. **Inventory Display Module:** Structured view showing full catalog data.
2. **Record Insertion Module:** Input interface appending valid catalog parameters dynamically.
3. **Status Toggle Engine:** Search and state modifier updating issuance availability flags.
4. **Analytical Lookup Engine:** Algorithmic routine calculating maximum entity attributes across parallel lists.
5. **Reverse Traversal Engine:** Index-based backward iterator rendering customized display logs.