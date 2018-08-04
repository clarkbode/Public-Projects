using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using GridMaster;

namespace Pathfinding
{
    public class Pathfinder
    {
        GridBase gridBase;
        public Node startPosition;
        public Node endPosition;

        public List<Node> FindPath() //the main function that will be called
        {
            //IMPORTANT: THIS IS NOT A MONOBEHAVIOR CLASS, SO WE CAN'T USE UNITY'S FUNCTIONS

            gridBase = GridBase.GetInstance();

            return FindPathActual(startPosition, endPosition);
        }

        private List<Node> FindPathActual(Node start, Node target)
        {
            // A* algorithm begins

            List<Node> foundPath = new List<Node>();


            // two lists, one for nodes we have not checked, and one for nodes we have.
            List<Node> openSet = new List<Node>();
            List<Node> closedSet = new HashSet<Node>(); //why error?

            //Start adding to open set
            openSet.Add(start);

            while (openSet.Count > 0)
            {
                Node currentNode = openSet[0];

                for (int i = 0; i < openSet.Count; i++) //could re-optimize this with a heap or something
                {
                    // check the costs for the current node
                    if (openSet[i].fCost < currentNode.fCost ||
                        (openSet[i].fCost == currentNode.fCost &&
                        openSet[i].hCost < currentNode.hCost))
                    {
                        //assign a new current node
                        if (!currentNode.Equals(openSet[i]))
                        {
                            currentNode = openSet[i];
                        }
                    }
                }
                // move current node from open set to closed set
                openSet.Remove(currentNode);
                closedSet.Add(currentNode);

                if (currentNode.Equals(target))
                {
                    // found destination, start retracing
                    foundPath = tracePath(start, currentNode);
                    break; // temp?
                }

                foreach (Node neighbor in GetNeighbors(currentNode, true))
                {
                    if (!closedSet.Contains(neighbor))
                    {
                        // new movement cost for neighbors
                        float newMovementCostToNeighbor = currentNode.gCost + GetDistance(currentNode, neighbor);

                        // if lower than neighbor cost
                        if (newMovementCostToNeighbor < neighbor.gCost || !openSet.Contains(neighbor))
                        {
                            // calculate the new costs
                            neighbor.gCost = newMovementCostToNeighbor;
                            neighbor.hCost = GetDistance(neighbor, target);

                            //Assign parent node
                            neighbor.parent = currentNode;
                            // BOOKMARK
                        }
                    }
                }
            }

            //return
        }


    }
}