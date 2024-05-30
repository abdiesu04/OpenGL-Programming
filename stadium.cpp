#include <GL/glut.h>
#include <cmath>

// Stadium dimensions
const float STADIUM_WIDTH = 100.0f;
const float STADIUM_HEIGHT = 50.0f;
const float STADIUM_DEPTH = 50.0f;

// Function to draw the stadium
void drawStadium() {
    glPushMatrix();

    // Draw the base of the stadium
    glColor3f(0.0f, 0.8f, 0.0f); // Set the color to green
    glBegin(GL_QUADS);
    glVertex3f(-STADIUM_WIDTH / 2, 0.0f, -STADIUM_DEPTH / 2);
    glVertex3f(-STADIUM_WIDTH / 2, 0.0f, STADIUM_DEPTH / 2);
    glVertex3f(STADIUM_WIDTH / 2, 0.0f, STADIUM_DEPTH / 2);
    glVertex3f(STADIUM_WIDTH / 2, 0.0f, -STADIUM_DEPTH / 2);
    glEnd();

    // Draw the walls of the stadium
    glColor3f(0.0f, 0.6f, 0.0f); // Set the color to a darker green for the walls
    glBegin(GL_QUADS);
    // Left wall
    glVertex3f(-STADIUM_WIDTH / 2, 0.0f, -STADIUM_DEPTH / 2);
    glVertex3f(-STADIUM_WIDTH / 2, 0.0f, STADIUM_DEPTH / 2);
    glVertex3f(-STADIUM_WIDTH / 2, STADIUM_HEIGHT, STADIUM_DEPTH / 2);
    glVertex3f(-STADIUM_WIDTH / 2, STADIUM_HEIGHT, -STADIUM_DEPTH / 2);
    // Right wall
    glVertex3f(STADIUM_WIDTH / 2, 0.0f, -STADIUM_DEPTH / 2);
    glVertex3f(STADIUM_WIDTH / 2, 0.0f, STADIUM_DEPTH / 2);
    glVertex3f(STADIUM_WIDTH / 2, STADIUM_HEIGHT, STADIUM_DEPTH / 2);
    glVertex3f(STADIUM_WIDTH / 2, STADIUM_HEIGHT, -STADIUM_DEPTH / 2);
    // Back wall
    glVertex3f(-STADIUM_WIDTH / 2, 0.0f, STADIUM_DEPTH / 2);
    glVertex3f(STADIUM_WIDTH / 2, 0.0f, STADIUM_DEPTH / 2);
    glVertex3f(STADIUM_WIDTH / 2, STADIUM_HEIGHT, STADIUM_DEPTH / 2);
    glVertex3f(-STADIUM_WIDTH / 2, STADIUM_HEIGHT, STADIUM_DEPTH / 2);
    // Front wall
    glVertex3f(-STADIUM_WIDTH / 2, 0.0f, -STADIUM_DEPTH / 2);
    glVertex3f(STADIUM_WIDTH / 2, 0.0f, -STADIUM_DEPTH / 2);
    glVertex3f(STADIUM_WIDTH / 2, STADIUM_HEIGHT, -STADIUM_DEPTH / 2);
    glVertex3f(-STADIUM_WIDTH / 2, STADIUM_HEIGHT, -STADIUM_DEPTH / 2);
    glEnd();

    glPopMatrix();
}

// Main function
int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(800, 600);
    glutCreateWindow("Stadium");

    glEnable(GL_DEPTH_TEST);

    glutDisplayFunc(drawStadium);
    glutMainLoop();

    return 0;
}