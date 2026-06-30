def validate_trip_speed(df):

    condition = df["trip_speed"] > 300

    df.loc[condition, "is_valid"] = False
    df.loc[condition, "validation_reason"] += "Invalid_trip_speed; "

    return df


def validate_trip_duration(df):

    condition = df["trip_duration"] > 300

    df.loc[condition, "is_valid"] = False
    df.loc[condition, "validation_reason"] += "Invalid_trip_duration; "

    return df


def validate_tip_percentage(df):

    condition = df["tip_percentage"] > 70

    df.loc[condition, "is_valid"] = False
    df.loc[condition, "validation_reason"] += "Invalid_trip_percentage; "

    return df


def validate_data(df):

    df["is_valid"] = True
    df["validation_reason"] = ""

    df = validate_trip_speed(df)
    df = validate_trip_duration(df)
    df = validate_tip_percentage(df)

    return df