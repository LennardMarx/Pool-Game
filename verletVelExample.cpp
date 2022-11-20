struct Body
{
    Vec3d pos { 0.0, 0.0, 0.0 };
    Vec3d vel { 2.0, 0.0, 0.0 }; // 2 m/s along x-axis
    Vec3d acc { 0.0, 0.0, 0.0 }; // no acceleration at first
    double mass = 1.0; // 1kg
    double drag = 0.1; // rho*C*Area – simplified drag for this example

    /**
     * Update pos and vel using "Velocity Verlet" integration
     * @param dt DeltaTime / time step [eg: 0.01]
     */
    void update(double dt)
    {
        Vec3d new_pos = pos + vel*dt + acc*(dt*dt*0.5);
        Vec3d new_acc = apply_forces(); // only needed if acceleration is not constant
        Vec3d new_vel = vel + (acc+new_acc)*(dt*0.5);
        pos = new_pos;
        vel = new_vel;
        acc = new_acc;
    }

    Vec3d apply_forces() const
    {
        Vec3d grav_acc = Vec3d{0.0, 0.0, -9.81 }; // 9.81 m/s² down in the z-axis
        Vec3d drag_force = 0.5 * drag * (vel * vel); // D = 0.5 * (rho * C * Area * vel^2)
        Vec3d drag_acc = drag_force / mass; // a = F/m
        return grav_acc - drag_acc;
    }
};