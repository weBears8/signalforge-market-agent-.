# Signing Agent HQ — Notion setup guide

The Notion version of your system. ~15 minutes to build, then it's yours forever.

## 1 · Import the databases
In Notion: **Import → CSV** and select each file in this folder, one at a time.
Each becomes its own database: **Signing Log, Mileage Log, Companies, Expenses.**

## 2 · Set the property types
Notion guesses types on import — fix them so filters and math work:

**Signing Log**
- Date → *Date* · Company → *Text* (or *Relation* to Companies, step 5)
- Order # / Borrower → *Text* · Appt type → *Select* · Status → *Select*
- Fee quoted / Fee paid / Miles / Print pages / Other cost → *Number*
- Paid → *Checkbox*

**Mileage Log:** Date → *Date* · Purpose/From/To → *Text* · Miles → *Number*
**Companies:** Avg fee / Pay speed / Rating → *Number* · the rest *Text*
**Expenses:** Date → *Date* · Category → *Select* · Amount → *Number* · Deductible → *Checkbox*

## 3 · Add the formula properties
Add a new property of type **Formula** and paste:

**Signing Log → `Net profit`**
```
prop("Fee paid") - (prop("Miles") * 0.70) - (prop("Print pages") * 0.1) - prop("Other cost")
```
**Mileage Log → `Deduction`**
```
prop("Miles") * 0.70
```
> `0.70` = the IRS standard mileage rate. **Update this number each January** in both
> formulas. (Advanced: keep the rate in a one-row "Settings" database and pull it in
> via a Relation + Rollup so you only change it once.)

## 4 · Create the Select options
On the *Status* property add: `Scheduled, Completed, Docs back, Invoiced, Paid, Cancelled`.
On *Appt type*: `Refi, Purchase, Seller, HELOC, Apostille, RON, Inspection, General`.
On Expenses *Category*: `Supplies, Insurance (E&O), Legal/Professional, Office,
Education/Training, Phone/Internet, Dues/Memberships, Software, Advertising/Marketing, Other`.

## 5 · (Recommended) Link the Signing Log to Companies
On Signing Log add a **Relation** property → Companies. Now each job points to a
company, and you can roll profit up per company on the Companies side.

## 6 · Create useful views (on the Signing Log)
- **Unpaid** — filter: `Paid` is unchecked AND `Status` is not `Cancelled`. Sort by Date.
- **This month** — filter: `Date` is within the current month.
- **By company** — *Board* or *Group by* Company.
- **Pipeline** — *Board* grouped by `Status`.

## 7 · Build the Dashboard page
Create a new page "Dashboard" and add **linked views** of each database
(type `/linked` → Create linked database). Then:
- On the Signing Log linked view, turn on **Calculate** at the bottom of the
  `Fee paid` and `Net profit` columns → `Sum`.
- On the Mileage Log linked view → `Sum` of `Miles` and `Deduction`.
- On Expenses → `Sum` of `Amount`.
That gives you fees paid, net profit, miles, deduction and expenses at a glance.

## 8 · Tax time
Filter Expenses by Category and read the sums; combine with the Mileage `Deduction`
sum and the Signing Log `Fee paid` sum. Hand those totals to your accountant against
Schedule C.

---
*This is an organizer, not tax advice. Confirm the current IRS rate and your
deductions with a professional. Single-user license — please don't redistribute.*
