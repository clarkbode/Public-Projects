using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace GridMaster
{

    public class GridBase : MonoBehaviour
    {

        // Grid setup
        public int maxX = 10;
        public int maxY = 3;
        public int maxZ = 10;

        // offset
        public float offsetX = 1;
        public float offsetY = 1;
        public float offsetZ = 1;

        public Node[,,] grid; //our grid

        public GameObject gridFloorPrefab;

        public Vector3 startNodePosition;
        public Vector3 endNodePosition;


        // Use this for initialization
        void Start()
        {

            grid = new Node[maxX, maxY, maxZ];

            for (int x = 0; x < maxX; x++)
            {
                for (int y = 0; y < maxY; y++)
                {
                    for (int z = 0; z < maxZ; z++)
                    {
                        // Apply offsets and create world object for a given Node
                        float posX = x * offsetX;
                        float posY = y * offsetY;
                        float posZ = z * offsetZ;

                        GameObject go = Instantiate(gridFloorPrefab, new Vector3(posX, posY, posZ), Quaternion.identity) as GameObject;

                        //name it after the values
                        go.transform.name = x.ToString() + " " + y.ToString() + " " + z.ToString();
                        // parent it under this transform
                        go.transform.parent = transform;

                        // New node with updated values
                        Node node = new Node();
                        node.x = x;
                        node.y = y;
                        node.z = z;
                        node.worldObject = go;

                        //place on the grid
                        grid[x, y, z] = node;
                    }
                }
            }
        }

        public bool start; //gross.

        // Update is called once per frame
        void Update()
        {
            if(start)
            {

            }
        }

        public Node GetNode(int x, int y, int z)
        {
            Node thing = null;

            if (x < maxX && x >= 0 &&
                y >= 0 && y < maxY &&
                z >= 0 && z < maxZ)
            {
                thing = grid[x, y, z];
            }

            return thing;
        }

        public Node GetNodeFromVector3(Vector3 pos)
        {
            int x = Mathf.RoundToInt(pos.x);
            int y = Mathf.RoundToInt(pos.y);
            int z = Mathf.RoundToInt(pos.z);

            Node thing = GetNode(x, y, z);
            return thing;
        }

        public static GridBase instance;
        public static GridBase GetInstance()
        {
            return instance;
        }

        private void Awake()
        {
            instance = this;
        }
    }
}