ArrayList<Planet> planets;
ArrayList<Star> stars;
Planet sun;
void setup() {
  size(1000, 860);
  planets = new ArrayList<Planet>();
  stars = new ArrayList<Star>();
  //angleMode(DEGREES);
  sun = new Planet(30, 0, 255, 0, 255);
  //shootingstar = new ShootingStar();
  for (int i = 0; i < 9; i++) {
    planets.add(new Planet(random(5, 11), (i + 1) * 44,random(255),random(255),random(255)));
  }
    for (int i = 0; i < 1000; i++) {
      stars.add(new Star());
    }
  
  }
void draw() {
  background(0);
 
  for (int i = 0; i < stars.size(); i++) {
      stars.get(i).show();
    }
  translate(width / 2, height / 2);
  sun.show();

  for (int i = 0; i < 9; i++) {
    push();
    rotate(planets.get(i).angle);
    translate(planets.get(i).distance, 0);

    planets.get(i).show();
    planets.get(i).orbit();
    pop();
  }
    
}
