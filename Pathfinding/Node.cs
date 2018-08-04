using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace GridMaster
{
    public class Node : MonoBehaviour
    {
        // Node's position
        public int x, y, z;

        // Node's cost
        public float hCost, gCost;

        // fCost is written this way for efficiency purposes. This way, fCost is not calculated each time something calls it.
        public float fCost 
        {
            get
            {
                return gCost + hCost;
            }
        }

        public Node parent;
        public bool walkable = true;

        //reference to the world object (not sure this is currently working, since the GameObject type isn't being highlighted
        public GameObject worldObject;

        public NodeType nodeType;
        public enum NodeType
        {
            ground,
            air
        }

    }
}


