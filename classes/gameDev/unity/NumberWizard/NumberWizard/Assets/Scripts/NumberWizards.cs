using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NumberWizards : MonoBehaviour {

    int max = 1000;
    int min = 1;
    int guess = 500;

    // Use this for initialization
    void Start ()
    {

        Debug.Log("Welcome to Number Wizards");
        Debug.Log("=========================");
        Debug.Log("Pick a number in your head and don't tell me.");

        Debug.Log("The highest number you can pick is " + max);
        Debug.Log("The lowest number you can pick is " + min);

        prompt();
    }

    private void prompt()
    {
        Debug.Log("Is the number higher or lower than " + guess + "?");
        Debug.Log("Press Up = higher, Push down = lower, return/enter = equal");
    }

    // Update is called once per frame
    void Update ()
	{
        // check key presses
		if (Input.GetKeyDown (KeyCode.UpArrow)) {
            // number is higher than guess so set the lower/min value to the guess
            Debug.Log("Up arrow pressed");
            min = guess;
            prompt();
        } else if (Input.GetKeyDown (KeyCode.DownArrow)) {
            // number is lower than guess so set the upper/max value to the guess
            Debug.Log("Down arrow pressed");
            max = guess;
            prompt();
        }
        else if (Input.GetKeyDown(KeyCode.Return))  // Enter / Return Key
        {
            Debug.Log("Enter pressed");
            min = 1;
            max = 1000;
            guess = 500;
        }
    }
}
