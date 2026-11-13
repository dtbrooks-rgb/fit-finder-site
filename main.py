from bakery import assert_equal
from dataclasses import dataclass
from drafter import *

set_site_information(
    author="dtbrooks@udel.edu",
    description= "FitFinder is a fitness website that helps users find exercises based on muscle group, available equipment, and difficulty level. Users can view exercise instructions and save their favorite exercises.",
    sources="Drafter documentation and AI assistance from ChatGPT.",
    planning=["design.pdf", "planning.pdf"],
    links=["https://github.com/dtbrooks-rgb/fit-finder-site"]
)
set_website_title("FitFinder")
hide_debug_information()
set_website_framed(False)

@dataclass
class Exercise:
    """Store information about an individual exercise."""
    name: str
    muscle_group: str
    difficulty: str
    equipment: str
    instructions: str


EXERCISES = [
    Exercise("Push-Up", "Chest", "Beginner", "No Equipment",
             "Start in a plank position. Lower your chest toward the floor and push back up."),
    Exercise("Dumbbell Chest Press", "Chest", "Beginner", "Dumbbells",
             "Lie on a bench and press dumbbells upward from your chest."),
    Exercise("Machine Chest Press", "Chest", "Beginner", "Machine",
             "Sit at the machine and push the handles forward."),
    Exercise("Resistance Band Chest Press", "Chest", "Beginner", "Resistance Bands",
             "Place a band behind your back and press your hands forward."),
    Exercise("Standing Cable Chest Press", "Chest", "Beginner", "Cables",
             "Stand between cable handles and press your arms forward."),
    Exercise("Incline Push-Up", "Chest", "Beginner", "No Equipment",
             "Place your hands on an elevated surface and perform a push-up."),
    Exercise("Incline Dumbbell Press", "Chest", "Intermediate", "Dumbbells",
             "Set a bench at an incline and press dumbbells upward."),
    Exercise("Barbell Bench Press", "Chest", "Intermediate", "Barbell",
             "Lower a barbell toward your chest and press it upward."),
    Exercise("Cable Chest Fly", "Chest", "Intermediate", "Cables",
             "Bring two cable handles together in front of your chest."),
    Exercise("Pec Deck Fly", "Chest", "Intermediate", "Machine",
             "Sit at the machine and bring the handles together."),
    Exercise("Dumbbell Pullover", "Chest", "Intermediate", "Dumbbells",
             "Lower a dumbbell behind your head while lying on a bench, then return."),
    Exercise("Resistance Band Chest Fly", "Chest", "Intermediate", "Resistance Bands",
             "Stretch a resistance band outward and bring your hands together."),
    Exercise("Decline Barbell Bench Press", "Chest", "Advanced", "Barbell",
             "Perform a controlled barbell press on a decline bench."),
    Exercise("Weighted Dip", "Chest", "Advanced", "Weighted Equipment",
             "Perform dips while using additional resistance."),
    Exercise("Incline Barbell Bench Press", "Chest", "Advanced", "Barbell",
             "Press a barbell upward while lying on an incline bench."),
    Exercise("Single Arm Cable Press", "Chest", "Advanced", "Cables",
             "Press one cable handle forward while maintaining a stable stance."),
    Exercise("Weighted Push-Up", "Chest", "Advanced", "Weighted Equipment",
             "Perform push-ups with safely secured additional resistance."),
    Exercise("Deficit Push-Up", "Chest", "Advanced", "No Equipment",
             "Perform push-ups with your hands elevated on stable handles."),
    Exercise("Lat Pulldown", "Back", "Beginner", "Machine",
             "Pull the bar toward your upper chest while seated."),
    Exercise("Dumbbell Row", "Back", "Beginner", "Dumbbells",
             "Bend forward and pull dumbbells toward your waist."),
    Exercise("Resistance Band Row", "Back", "Beginner", "Resistance Bands",
             "Pull a resistance band toward your body while seated."),
    Exercise("Assisted Pull-Up", "Back", "Beginner", "Machine",
             "Use an assisted pull-up machine to pull your body upward."),
    Exercise("Seated Cable Row", "Back", "Beginner", "Cables",
             "Pull the cable handle toward your stomach."),
    Exercise("Bird Dog", "Back", "Beginner", "No Equipment",
             "Extend opposite arm and leg while keeping your torso stable."),

    Exercise("Barbell Bent-Over Row", "Back", "Intermediate", "Barbell",
             "Hinge forward and pull the barbell toward your waist."),
    Exercise("Single Arm Dumbbell Row", "Back", "Intermediate", "Dumbbells",
             "Support yourself on a bench and pull one dumbbell toward your hip."),
    Exercise("Cable Face Pull", "Back", "Intermediate", "Cables",
             "Pull a rope attachment toward your face."),
    Exercise("Dumbbell Deadlift", "Back", "Intermediate", "Dumbbells",
             "Hold dumbbells and hinge at your hips before standing upright."),
    Exercise("Straight Arm Pulldown", "Back", "Intermediate", "Cables",
             "Pull a cable bar down while keeping your arms mostly straight."),
    Exercise("Resistance Band Pulldown", "Back", "Intermediate", "Resistance Bands",
             "Pull a resistance band downward while maintaining control."),
    Exercise("Weighted Pull-Up", "Back", "Advanced", "Weighted Equipment",
             "Perform a pull-up with safely secured additional resistance."),
    Exercise("Pendlay Row", "Back", "Advanced", "Barbell",
             "Perform controlled barbell rows from a hinged position."),
    Exercise("Renegade Row", "Back", "Advanced", "Dumbbells",
             "Hold a plank position and alternate rowing each dumbbell."),
    Exercise("Rack Pull", "Back", "Advanced", "Barbell",
             "Lift a barbell from an elevated starting position."),
    Exercise("Single Arm Cable Row", "Back", "Advanced", "Cables",
             "Perform a controlled one-arm cable row."),
    Exercise("Inverted Row", "Back", "Advanced", "No Equipment",
             "Hang beneath a secure horizontal bar and pull your chest toward it."),
    Exercise("Dumbbell Shoulder Press", "Shoulders", "Beginner", "Dumbbells",
             "Press dumbbells overhead from shoulder height."),
    Exercise("Machine Shoulder Press", "Shoulders", "Beginner", "Machine",
             "Sit at the machine and press the handles overhead."),
    Exercise("Resistance Band Lateral Raise", "Shoulders", "Beginner", "Resistance Bands",
             "Raise your arms outward against resistance."),
    Exercise("Dumbbell Front Raise", "Shoulders", "Beginner", "Dumbbells",
             "Raise dumbbells in front of your body to shoulder height."),
    Exercise("Cable Lateral Raise", "Shoulders", "Beginner", "Cables",
             "Raise one arm outward using a cable attachment."),
    Exercise("Arm Circles", "Shoulders", "Beginner", "No Equipment",
             "Extend your arms and make controlled circular movements."),
    Exercise("Arnold Press", "Shoulders", "Intermediate", "Dumbbells",
             "Rotate your hands while pressing dumbbells overhead."),
    Exercise("Barbell Overhead Press", "Shoulders", "Intermediate", "Barbell",
             "Press a barbell overhead from shoulder height."),
    Exercise("Dumbbell Lateral Raise", "Shoulders", "Intermediate", "Dumbbells",
             "Raise dumbbells outward until your arms reach shoulder height."),
    Exercise("Cable Face Pull", "Shoulders", "Intermediate", "Cables",
             "Pull a rope attachment toward your face."),
    Exercise("Reverse Pec Deck", "Shoulders", "Intermediate", "Machine",
             "Move your arms backward against the machine's resistance."),
    Exercise("Resistance Band Shoulder Press", "Shoulders", "Intermediate", "Resistance Bands",
             "Stand on a resistance band and press your hands overhead."),
    Exercise("Seated Barbell Shoulder Press", "Shoulders", "Advanced", "Barbell",
             "Perform a controlled overhead barbell press while seated."),
    Exercise("Dumbbell Push Press", "Shoulders", "Advanced", "Dumbbells",
             "Use a slight knee bend to help drive dumbbells overhead."),
    Exercise("Cable Upright Row", "Shoulders", "Advanced", "Cables",
             "Pull a cable attachment upward with controlled movement."),
    Exercise("Handstand Push-Up", "Shoulders", "Advanced", "No Equipment",
             "Perform a controlled vertical push-up against a suitable stable surface."),
    Exercise("Single Arm Landmine Press", "Shoulders", "Advanced", "Barbell",
             "Press the end of a secured barbell upward with one arm."),
    Exercise("Heavy Dumbbell Lateral Raise", "Shoulders", "Advanced", "Dumbbells",
             "Perform controlled lateral raises using challenging resistance."),
    Exercise("Dumbbell Bicep Curl", "Arms", "Beginner", "Dumbbells",
             "Curl dumbbells toward your shoulders while keeping your elbows close."),
    Exercise("Cable Tricep Pushdown", "Arms", "Beginner", "Cables",
             "Push a cable attachment downward until your arms extend."),
    Exercise("Machine Bicep Curl", "Arms", "Beginner", "Machine",
             "Curl the machine handles toward your shoulders."),
    Exercise("Resistance Band Bicep Curl", "Arms", "Beginner", "Resistance Bands",
             "Stand on a resistance band and curl your hands upward."),
    Exercise("Dumbbell Hammer Curl", "Arms", "Beginner", "Dumbbells",
             "Curl dumbbells with your palms facing inward."),
    Exercise("Knee Push-Up", "Arms", "Beginner", "No Equipment",
             "Perform a modified push-up from your knees."),
    Exercise("Barbell Bicep Curl", "Arms", "Intermediate", "Barbell",
             "Curl a barbell toward your shoulders without swinging."),
    Exercise("Overhead Tricep Extension", "Arms", "Intermediate", "Dumbbells",
             "Lower a dumbbell behind your head and extend your arms."),
    Exercise("Cable Bicep Curl", "Arms", "Intermediate", "Cables",
             "Curl a cable handle toward your shoulders."),
    Exercise("Tricep Rope Extension", "Arms", "Intermediate", "Cables",
             "Push a rope attachment downward and separate the ends."),
    Exercise("Dumbbell Concentration Curl", "Arms", "Intermediate", "Dumbbells",
             "Sit and curl one dumbbell while supporting your upper arm."),
    Exercise("Close-Grip Push-Up", "Arms", "Intermediate", "No Equipment",
             "Perform push-ups with your hands closer together."),
    Exercise("EZ-Bar Skull Crusher", "Arms", "Advanced", "Barbell",
             "Lower an EZ-bar toward your forehead while lying on a bench."),
    Exercise("Weighted Chin-Up", "Arms", "Advanced", "Weighted Equipment",
             "Perform chin-ups with safely secured additional resistance."),
    Exercise("Dumbbell Skull Crusher", "Arms", "Advanced", "Dumbbells",
             "Lower dumbbells toward the sides of your head while lying down."),
    Exercise("Cable Overhead Tricep Extension", "Arms", "Advanced", "Cables",
             "Extend both arms overhead against cable resistance."),
    Exercise("Preacher Curl", "Arms", "Advanced", "Machine",
             "Perform controlled curls using a preacher curl machine."),
    Exercise("Diamond Push-Up", "Arms", "Advanced", "No Equipment",
             "Perform a push-up with your hands close together beneath your chest."),
    Exercise("Bodyweight Squat", "Legs", "Beginner", "No Equipment",
             "Stand with feet shoulder-width apart and squat down."),
    Exercise("Leg Press", "Legs", "Beginner", "Machine",
             "Push the machine platform away using your legs."),
    Exercise("Dumbbell Goblet Squat", "Legs", "Beginner", "Dumbbells",
             "Hold a dumbbell at your chest and perform a squat."),
    Exercise("Resistance Band Squat", "Legs", "Beginner", "Resistance Bands",
             "Stand on a resistance band and perform controlled squats."),
    Exercise("Dumbbell Step-Up", "Legs", "Beginner", "Dumbbells",
             "Step onto a stable platform while holding dumbbells."),
    Exercise("Standing Calf Raise", "Legs", "Beginner", "No Equipment",
             "Rise onto your toes and slowly lower your heels."),
    Exercise("Barbell Back Squat", "Legs", "Intermediate", "Barbell",
             "Place a barbell across your upper back and perform a squat."),
    Exercise("Dumbbell Romanian Deadlift", "Legs", "Intermediate", "Dumbbells",
             "Hinge at your hips while holding dumbbells in front of your legs."),
    Exercise("Leg Extension", "Legs", "Intermediate", "Machine",
             "Extend your knees against the machine's resistance."),
    Exercise("Cable Leg Kickback", "Legs", "Intermediate", "Cables",
             "Extend one leg backward against cable resistance."),
    Exercise("Walking Lunges", "Legs", "Intermediate", "Dumbbells",
             "Take alternating steps forward into controlled lunges."),
    Exercise("Resistance Band Lateral Walk", "Legs", "Intermediate", "Resistance Bands",
             "Walk sideways while keeping tension on a resistance band."),
    Exercise("Barbell Front Squat", "Legs", "Advanced", "Barbell",
             "Hold a barbell in front of your shoulders and perform a squat."),
    Exercise("Bulgarian Split Squat", "Legs", "Advanced", "Dumbbells",
             "Place one foot behind you on a bench and lower into a split squat."),
    Exercise("Barbell Romanian Deadlift", "Legs", "Advanced", "Barbell",
             "Hinge at your hips while holding a barbell."),
    Exercise("Single Leg Leg Press", "Legs", "Advanced", "Machine",
             "Perform a controlled leg press using one leg at a time."),
    Exercise("Jump Squat", "Legs", "Advanced", "No Equipment",
             "Perform a squat and jump upward before landing softly."),
    Exercise("Cable Pull-Through", "Legs", "Advanced", "Cables",
             "Hinge at your hips while pulling a low cable attachment forward."),
    Exercise("Basic Plank", "Core", "Beginner", "No Equipment",
             "Hold a straight-body position supported by your forearms and toes."),
    Exercise("Dumbbell Side Bend", "Core", "Beginner", "Dumbbells",
             "Hold a dumbbell at your side and bend sideways in a controlled manner."),
    Exercise("Machine Ab Crunch", "Core", "Beginner", "Machine",
             "Use the machine to perform controlled abdominal crunches."),
    Exercise("Resistance Band Crunch", "Core", "Beginner", "Resistance Bands",
             "Perform crunches while holding a resistance band for added tension."),
    Exercise("Medicine Ball Crunch", "Core", "Beginner", "Medicine Ball",
             "Hold a medicine ball at your chest while performing crunches."),
    Exercise("Dead Bug", "Core", "Beginner", "No Equipment",
             "Lie on your back and extend opposite arms and legs while keeping your core engaged."),
    Exercise("Weighted Russian Twist", "Core", "Intermediate", "Dumbbells",
             "Sit with knees bent and rotate your torso while holding a dumbbell."),
    Exercise("Cable Woodchop", "Core", "Intermediate", "Cables",
             "Rotate your torso while pulling a cable diagonally across your body."),
    Exercise("Medicine Ball Slams", "Core", "Intermediate", "Medicine Ball",
             "Raise a medicine ball overhead and slam it safely onto the floor."),
    Exercise("Hanging Knee Raise", "Core", "Intermediate", "No Equipment",
             "Hang from a bar and raise your knees toward your chest."),
    Exercise("Resistance Band Pallof Press", "Core", "Intermediate", "Resistance Bands",
             "Press a resistance band forward while resisting rotation."),
    Exercise("Ab Crunch Machine", "Core", "Intermediate", "Machine",
             "Perform controlled repetitions using an abdominal machine."),
    Exercise("Hanging Leg Raise", "Core", "Advanced", "No Equipment",
             "Hang from a bar and raise your straight legs with control."),
    Exercise("Weighted Decline Sit-Up", "Core", "Advanced", "Weighted Equipment",
             "Perform a decline sit-up while holding additional resistance."),
    Exercise("Dumbbell Turkish Get-Up", "Core", "Advanced", "Dumbbells",
             "Move from lying down to standing while holding a dumbbell overhead."),
    Exercise("Cable Crunch", "Core", "Advanced", "Cables",
             "Kneel at a cable machine and curl your torso downward."),
    Exercise("Medicine Ball V-Up", "Core", "Advanced", "Medicine Ball",
             "Raise your arms and legs together while holding a medicine ball."),
    Exercise("Weighted Plank", "Core", "Advanced", "Weighted Equipment",
             "Hold a plank position with safely secured additional resistance.")
]



MUSCLE_GROUPS = ["Any", "Chest","Back","Shoulders","Arms","Legs","Core"]
EQUIPMENT_OPTIONS = ["Any","Dumbbells","Barbell","Machine","Cables","Resistance Bands","Medicine Ball","No Equipment","Weighted Equipment"]
DIFFICULTY_OPTIONS = ["Any","Beginner","Intermediate","Advanced"]

@dataclass
class State:
    """Store information used throughout FitFinder."""
    selected_muscle: str
    selected_equipment: str
    selected_difficulty: str
    selected_exercise_name: str
    exercises: list[Exercise]
    matching_exercises: list[Exercise]
    favorites: list[Exercise]

def add_navigation(content: list) -> None:
    """Add navigation links to a page."""
    content.extend([
        Link("Home", "index"),
        " | ",
        Link("Find Exercises", "find_exercises"),
        " | ",
        Link("Favorites", "favorites"),
        " | ",
        Link("About", "about"),
        HorizontalRule()
    ])

def find_exercise_by_name(exercises: list[Exercise], exercise_name: str) -> Exercise | None:
    """Find an exercise using its name."""
    for exercise in exercises:
        if exercise.name == exercise_name:
            return exercise
    return None

# Unit tests for find_exercise_by_name
assert_equal(find_exercise_by_name(EXERCISES, "Push-Up"),EXERCISES[0])
assert_equal(find_exercise_by_name(EXERCISES, "Barbell Bench Press"),EXERCISES[7])
assert_equal(find_exercise_by_name(EXERCISES, "Cable Face Pull"),EXERCISES[26])
assert_equal(find_exercise_by_name(EXERCISES, "Not An Exercise"),None)
    
def filter_exercises(
    exercises: list[Exercise],
    muscle: str,
    equipment: str,
    difficulty: str,
    search_name: str
    ) -> list[Exercise]:
    """Return exercises matching all selected filters."""
    matching = []
    for exercise in exercises:
        muscle_matches = (muscle == "Any" or exercise.muscle_group == muscle)
        equipment_matches = (equipment == "Any" or exercise.equipment == equipment)
        difficulty_matches = (difficulty == "Any" or exercise.difficulty == difficulty)
        name_matches = (search_name.strip().lower() in exercise.name.lower())
        if (muscle_matches and equipment_matches and difficulty_matches and name_matches):
            matching.append(exercise)
    return matching

# Unit tests for filter_exercises
assert_equal(filter_exercises(EXERCISES, "Any", "Any", "Any", ""), EXERCISES)
assert_equal(filter_exercises(EXERCISES, "Chest", "Any", "Any", ""),EXERCISES[0:18])
assert_equal(filter_exercises(EXERCISES, "Chest", "Any", "Beginner", ""),EXERCISES[0:6])
assert_equal(filter_exercises(EXERCISES, "Chest", "Any", "Advanced", ""),EXERCISES[12:18])
assert_equal(filter_exercises(EXERCISES, "Chest", "Dumbbells", "Any", ""),[EXERCISES[1],EXERCISES[6],EXERCISES[10]])
assert_equal(filter_exercises(EXERCISES, "Chest", "Barbell", "Advanced", ""), [EXERCISES[12], EXERCISES[14]])
assert_equal(filter_exercises(EXERCISES, "Chest", "Any", "Any", "Push-Up"),[EXERCISES[0],EXERCISES[5],EXERCISES[16],EXERCISES[17]])
assert_equal(filter_exercises(EXERCISES, "Chest", "Any", "Any", "PUSH-UP"),[EXERCISES[0],EXERCISES[5],EXERCISES[16],EXERCISES[17]])
assert_equal(filter_exercises(EXERCISES, "Chest", "Any", "Any", "  Push-Up  "),[EXERCISES[0],EXERCISES[5],EXERCISES[16],EXERCISES[17]])
assert_equal(filter_exercises(EXERCISES, "Chest", "Dumbbells", "Beginner", ""),[EXERCISES[1]])
assert_equal(filter_exercises(EXERCISES, "Chest", "Machine", "Advanced", ""),[])
assert_equal(filter_exercises(EXERCISES, "Chest", "Any", "Any", "Swimming"),[])

def add_exercise_to_favorites(favorite_list: list[Exercise],exercise: Exercise) -> None:
    """Add an exercise without removing existing favorites."""
    already_saved = False
    for saved_exercise in favorite_list:
        if saved_exercise.name == exercise.name:
            already_saved = True
    if not already_saved:
        favorite_list.append(exercise)

def remove_exercise_from_favorites(favorite_list: list[Exercise],exercise_name: str) -> list[Exercise]:
    """Remove only the selected exercise from favorites."""
    remaining = []
    for exercise in favorite_list:
        if exercise.name != exercise_name:
            remaining.append(exercise)
    return remaining

# Unit tests for remove_exercise_from_favorites
assert_equal(remove_exercise_from_favorites
             ([EXERCISES[0], EXERCISES[1], EXERCISES[2]],"Push-Up"),
             [EXERCISES[1], EXERCISES[2]])
assert_equal(remove_exercise_from_favorites
             ([EXERCISES[0], EXERCISES[1]],"Not An Exercise"),
             [EXERCISES[0], EXERCISES[1]])
assert_equal(remove_exercise_from_favorites([EXERCISES[0]],"Push-Up"),[])
assert_equal(remove_exercise_from_favorites([], "Push-Up"),[])

@route
def index(state: State) -> Page:
    """Display the FitFinder homepage."""
    content = [Header("Welcome to FitFinder!")]
    add_navigation(content)
    content.extend([
        Header("Find Your Next Exercise"),
        "Welcome to FitFinder, your exercise discovery tool!",
        "Find exercises based on your target muscle group, "
        "available equipment, and preferred difficulty.",
        "Explore exercises, learn how to perform them, "
        "and save as many favorites as you want.",
        HorizontalRule(),
        Button("Find Exercises", "find_exercises"),
        Button("View My Favorites", "favorites")
    ])
    return Page(state, content)
# Unit test for index
assert_equal(type(index(State
    ("Any", "Any", "Any", "",EXERCISES.copy(), [], []))),Page)

@route
def find_exercises(state: State) -> Page:
    """Display the exercise search form."""
    content = [Header("Find Exercises")]
    add_navigation(content)
    content.extend([
        "Select a muscle group:",
        SelectBox(
            "selected_muscle",
            MUSCLE_GROUPS,
            state.selected_muscle
        ),
        "Select your available equipment:",
        SelectBox(
            "selected_equipment",
            EQUIPMENT_OPTIONS,
            state.selected_equipment
        ),
        "Select your preferred difficulty:",
        SelectBox(
            "selected_difficulty",
            DIFFICULTY_OPTIONS,
            state.selected_difficulty
        ),
        "Search for a specific exercise (optional):",
        TextBox(
            "exercise_name",
            state.selected_exercise_name
        ),
        HorizontalRule(),
        Button("Search Exercises", "exercise_results")
    ])
    return Page(state, content)

# Unit test for find_exercises
assert_equal(type(find_exercises(State("Any", "Any", "Any", "",EXERCISES.copy(), [], []))),Page)


@route
def exercise_results(
    state: State,
    selected_muscle: str,
    selected_equipment: str,
    selected_difficulty: str,
    exercise_name: str
) -> Page:
    """Display exercises matching the user's search."""
    state.selected_muscle = selected_muscle
    state.selected_equipment = selected_equipment
    state.selected_difficulty = selected_difficulty
    state.selected_exercise_name = exercise_name
    state.matching_exercises = filter_exercises(
        state.exercises,
        selected_muscle,
        selected_equipment,
        selected_difficulty,
        exercise_name
    )
    content = [Header("Exercise Results")]
    add_navigation(content)
    content.append("Here are your matching exercises:")
    if len(state.matching_exercises) == 0:
        content.append("No exercises matched your search. ""Try changing your selections.")
    else:
        content.append(
            "Number of matching exercises: "
            + str(len(state.matching_exercises))
        )

        for exercise in state.matching_exercises:
            content.extend([
                Header(exercise.name),
                "Muscle Group: " + exercise.muscle_group,
                "Equipment: " + exercise.equipment,
                "Difficulty: " + exercise.difficulty,
                Button(
                    "View Exercise Details",
                    "exercise_details",
                    [
                        Argument("exercise_name", exercise.name)
                    ]
                ),
                HorizontalRule()])
    content.append(Button("Search Again", "find_exercises"))
    return Page(state, content)


@route
def exercise_details(state: State,exercise_name: str) -> Page:
    """Display information about a selected exercise."""
    exercise = find_exercise_by_name(state.exercises,exercise_name)
    content = [Header("Exercise Details")]
    add_navigation(content)
    if exercise is None:
        content.extend([
            "Sorry, this exercise could not be found.",
            Button("Find Exercises", "find_exercises")
        ])

        return Page(state, content)

    content.extend([
        Header(exercise.name),
        "Muscle Group: " + exercise.muscle_group,
        "Difficulty: " + exercise.difficulty,
        "Equipment Needed: " + exercise.equipment,
        Header("Instructions"),
        exercise.instructions,
        HorizontalRule()
    ])

    if exercise in state.favorites:
        content.extend([
            "This exercise is already in your favorites.",
            Button(
                "Remove from Favorites",
                "remove_favorite",
                [Argument("exercise_name", exercise.name)])])

    else:
        content.append(
            Button(
                "Add to Favorites",
                "add_favorite",
                [Argument("exercise_name", exercise.name)]))

    content.append(
        Button(
            "Back to Exercise Results",
            "exercise_results",
            [
                Argument("selected_muscle", state.selected_muscle),
                Argument("selected_equipment", state.selected_equipment),
                Argument("selected_difficulty", state.selected_difficulty),
                Argument("exercise_name", state.selected_exercise_name)
            ]))

    return Page(state, content)

@route
def add_favorite(state: State,exercise_name: str) -> Page:
    """Add an exercise to the user's favorites."""
    exercise = find_exercise_by_name(state.exercises,exercise_name)
    if exercise is not None:
        add_exercise_to_favorites(
            state.favorites,
            exercise
        )

    return favorites(state)

@route
def favorites(state: State) -> Page:
    """Display all exercises saved by the user."""

    content = [Header("My Favorite Exercises")]
    add_navigation(content)
    content.append(
        "You have saved "
        + str(len(state.favorites))
        + " favorite exercise(s)."
    )

    if len(state.favorites) == 0:
        content.extend([
            "You have not saved any favorite exercises yet.",
            Button("Find Exercises", "find_exercises")
        ])

    else:
        for exercise in state.favorites:
            content.extend([
                Header(exercise.name),
                "Muscle Group: " + exercise.muscle_group,
                "Equipment: " + exercise.equipment,
                "Difficulty: " + exercise.difficulty,
                Button(
                    "View Exercise Details",
                    "exercise_details",
                    [Argument("exercise_name", exercise.name)]
                ),
                Button(
                    "Remove Favorite",
                    "remove_favorite",
                    [Argument("exercise_name", exercise.name)]
                ),
                HorizontalRule()
            ])
        content.append(
            Button("Continue Finding Exercises", "find_exercises"))
    return Page(state, content)

# Unit tests for favorites

assert_equal(
    type(favorites(State(
        "Any", "Any", "Any", "",
        EXERCISES.copy(), [], []
    ))),
    Page)
assert_equal(
    type(favorites(State(
        "Any", "Any", "Any", "",
        EXERCISES.copy(), [],
        [EXERCISES[0], EXERCISES[1]]
    ))),
    Page)


@route
def remove_favorite(state: State,exercise_name: str) -> Page:
    """Remove one exercise without affecting other favorites."""
    state.favorites = remove_exercise_from_favorites(
        state.favorites,
        exercise_name)
    return favorites(state)


@route
def about(state: State) -> Page:
    """Explain the purpose of FitFinder."""
    content = [Header("About FitFinder")]
    add_navigation(content)
    content.extend([
        Header("Our Purpose"),
        "FitFinder was created to make finding exercises "
        "easier for people who want to improve their fitness.",
        "Users can search for exercises based on their "
        "target muscle group, available equipment, and difficulty.",
        Header("What You Can Do"),
        "1. Search for exercises.",
        "2. Filter by muscle group.",
        "3. Filter by equipment.",
        "4. Filter by difficulty.",
        "5. View exercise instructions.",
        "6. Save and remove as many favorite exercises as you want.",
        HorizontalRule(),
        "Thank you for using FitFinder!"
    ])
    return Page(state, content)

# Unit test for about
assert_equal(
    type(about(State(
        "Any", "Any", "Any", "",
        EXERCISES.copy(), [], []
    ))),
    Page)

#I realized I was using global variables to test these functions. 
#So instead I made them into functions and tested them that way.
#So all the functions up to that are missing unit tests after them they are now right here.
def test_add_navigation():
    """Test that navigation links are added to a page."""
    navigation_content = ["Existing Content"]

    assert_equal(add_navigation(navigation_content), None)
    assert_equal(navigation_content,
        [
            "Existing Content",
            Link("Home", "index"),
            " | ",
            Link("Find Exercises", "find_exercises"),
            " | ",
            Link("Favorites", "favorites"),
            " | ",
            Link("About", "about"),
            HorizontalRule()
        ])


def test_add_exercise_to_favorites():
    """Test adding favorites and preventing duplicates."""
    favorite_test = [EXERCISES[1]]

    assert_equal(add_exercise_to_favorites(favorite_test, EXERCISES[0]), None)
    assert_equal(favorite_test, [EXERCISES[1], EXERCISES[0]])

    add_exercise_to_favorites(favorite_test, EXERCISES[0])
    assert_equal(favorite_test, [EXERCISES[1], EXERCISES[0]])

    add_exercise_to_favorites(favorite_test, EXERCISES[2])
    assert_equal(favorite_test, [EXERCISES[1], EXERCISES[0], EXERCISES[2]])


def test_exercise_results():
    """Test that exercise results update the user's search selections."""
    test_state = State("Any", "Any", "Any", "", EXERCISES.copy(), [], [])

    result_page = exercise_results(test_state, "Chest", "Dumbbells", "Beginner", "")

    assert_equal(type(result_page), Page)
    assert_equal(test_state.selected_muscle, "Chest")
    assert_equal(test_state.selected_equipment, "Dumbbells")
    assert_equal(test_state.selected_difficulty, "Beginner")
    assert_equal(test_state.selected_exercise_name, "")
    assert_equal(test_state.matching_exercises, [EXERCISES[1]])


def test_exercise_details():
    """Test displaying exercise details for existing and missing exercises."""
    test_state = State("Any", "Any", "Any", "", EXERCISES.copy(), [], [])

    assert_equal(type(exercise_details(test_state, "Push-Up")), Page)
    assert_equal(type(exercise_details(test_state, "Not An Exercise")), Page)


def test_add_favorite():
    """Test adding multiple favorites and preventing duplicates."""
    test_state = State("Any", "Any", "Any", "", EXERCISES.copy(), [], [])

    assert_equal(type(add_favorite(test_state, "Push-Up")), Page)
    assert_equal(test_state.favorites, [EXERCISES[0]])

    add_favorite(test_state, "Dumbbell Chest Press")
    assert_equal(test_state.favorites, [EXERCISES[0], EXERCISES[1]])

    add_favorite(test_state, "Push-Up")
    assert_equal(test_state.favorites, [EXERCISES[0], EXERCISES[1]])

    add_favorite(test_state, "Not An Exercise")
    assert_equal(test_state.favorites, [EXERCISES[0], EXERCISES[1]])


def test_remove_favorite():
    """Test removing favorites without affecting other saved exercises."""
    test_state = State(
        "Any", "Any", "Any", "",
        EXERCISES.copy(), [],
        [EXERCISES[0], EXERCISES[1], EXERCISES[2]]
    )

    assert_equal(type(remove_favorite(test_state, "Push-Up")), Page)
    assert_equal(test_state.favorites, [EXERCISES[1], EXERCISES[2]])

    remove_favorite(test_state, "Not An Exercise")
    assert_equal(test_state.favorites, [EXERCISES[1], EXERCISES[2]])

# Run the unit test functions
test_add_navigation()
test_add_exercise_to_favorites()
test_exercise_results()
test_exercise_details()
test_add_favorite()
test_remove_favorite()


start_server(State("Any","Any","Any","",EXERCISES.copy(),[],[]))
