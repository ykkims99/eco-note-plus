
// EcoNote+ Enclosure Top (simplified functional model)
$fn=80;
difference() {
  cube([120, 90, 10], center=false);  // Main top shell
  translate([10, 10, -1]) cube([100, 70, 12]); // hollow cut
}
