using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class AdventureGame : MonoBehaviour {

    [SerializeField] Text textComponent;

	// Use this for initialization
	void Start () {
        textComponent.text = ("These are the adventures of Ace Burrows, seeker of artifacts of great value and significance.  Always escaping from extreme dangers and obstacles");
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
