from user import users, find_matches

def admin_view():
    print("Admin View:")
    print("User Profiles:")
    for user, data in users.items():
        print(f"{user}: {data['profile']}")
    print("\nUser Preferences:")
    for user, data in users.items():
        print(f"{user}: {data['preferences']}")
    print("\nMatches:")
    matches = find_matches()
    for user, match_list in matches.items():
        print(f"{user} matches with: {', '.join(match_list) if match_list else 'No matches found'}")
