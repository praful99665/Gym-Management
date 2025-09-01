# Gym Management

A custom Frappe app to manage gym members, subscriptions, and payments efficiently.

## Features
- Manage Gym Members
- Handle Membership Plans and Subscriptions
- Track Workout Sessions
- Manage Payments and Invoices
- Notifications
- Integration with ERPNext for accounting

## Installation
1. Get the app:
   ```bash
   bench get-app https://github.com/praful99665/Gym-Management.git
   bench --site yoursite-name install-app gym_management
   bench --site yoursite-name migrate
   bench restart
