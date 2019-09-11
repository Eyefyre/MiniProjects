class Planet{
  float radius,angle,orbitspeed,red,blue,green;
  int distance;
  
  Planet(float radius,int distance,float red,float blue,float green){
    this.radius = radius;
    this.angle = random(360);
    this.distance = distance;
    this.orbitspeed = random(0.01,0.03);
    this.red = red;
    this.blue = blue;
    this.green = green;
  }

  void show() {
    fill(this.red, this.green, this.blue);
    ellipse(0, 0, this.radius * 2, this.radius * 2);
  };

  void orbit() {
    this.angle -= this.orbitspeed;
  };
}
