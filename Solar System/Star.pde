class Star{
  PVector pos;
  float radius;
  
  Star(){
   this.pos = new PVector(random(width),random(height));
   this.radius = random(1,2);
  }
  
  void show()
  {
    ellipse(this.pos.x, this.pos.y, this.radius*2,this.radius*2);
  }
}
