
// EcoNote+ Enclosure Bottom
$fn=80;
difference() {
  cube([120, 90, 15], center=false); // Base block
  translate([15, 15, 0]) cube([90, 60, 12]); // main cavity
  // screw holes
  for (x = [10, 110]) {
    for (y = [10, 80]) {
      translate([x, y, 0]) cylinder(h=15, r=2);
    }
  }
}
