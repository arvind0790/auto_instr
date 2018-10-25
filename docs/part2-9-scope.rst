====================================
scope- Digital Phosphor Oscilloscope
====================================

This class is written for Tektronix Digital Phosphor Oscilloscope 7104. It supports following methods.

----------------
Channel settings
----------------
- **channel_offset(instr,ch_no, v_offset)**, sets the offset of a given channel.
- **channel_scale(instr,ch_no, v_scale)**, sets the vertical scale.
- **horz_scale(instr,scale)**, sets the horizontal scale.
- **bandwidth_full(instr,ch_no)**, sets the maximum bandwidth.
- **set_bandwidth(instr,ch_no,bw)**, sets the bandwidth to a given value.
- **autoset(instr)**, auto sets the scope.
- **set_abs_ref_lev(instr,abs_min_ref_lev,abs_max_ref_lev)**, sets the absolute reference levels used for rise fall delay measurements.
- **set_perc_ref_lev(instr,perc_min_ref_lev,perc_max_ref_lev)**, sets the percentage reference levels used for rise fall measurements.

--------------------
Acquisition settings
--------------------
- **run(instr)**, starts the acquisitions.
- **stop(instr)**, stops acquisitions.
- **run_mode(instr)**, configures the scope in continuous run mode. 
- **single(instr)**, configures the in single acquisition mode.
- **single_refresh(instr)**, turns on the previously set acquisition mode.
- **averaging(instr,no_avg)**, configures in the averaging mode.
- **high_resolution(instr)**, configures in high resolution mode.
- **single_acquisition_quickset(instr,ch_no,lev,edge)**, clears measurements, sets the trigger and starts the single mode acquisition.

----------------
Trigger settings
----------------
- **trigger_quickset_rise(instr, ch_no,lev)**, sets the rising edge trigger level for a given channel. 
- **trigger_quickset_fall(instr, ch_no,lev)**, sets the falling edge trigger level for a given channel. 

---------------------
Measurement functions
---------------------
- **meas_cls(instr)**, clears the previous measurements.
- **measure_source(instr,ch_no)**, sets the given channel as default channel for measurements.
- **measure_amp(instr)**, measures immediate amplitude of the default channel.
- **measure_high(instr)**, measure immediate high value.
- **measure_low(instr)**, measures immediate low value.
- **measure_freq(instr)**, measures immediate frequency value.
- **measure_positive_duty(instr)**, measures immediate positive duty cycle. 
- **measure_negative_duty(instr)**, measures immediate negative duty cycle.
- **measure_rise_time(instr)**, measures immediate rise time.
- **measure_fall_time(instr)**,measures immediate fall time. 
- **measure_positive_pulse_width(instr)**, measures immediate positive pulse width.
- **measure_negative_pulse_width(instr)**, measures immediate negative pulse width.
- **delay(instr, ch1=1, ch2=2,edge_ch1 = 'RISE',edge_ch2 = 'FALL',direction ='FORW')**, measures delay between two channels for given edge type and direction.

------------------------------------------
DPOJET functions (for jitter measurements)
------------------------------------------
- **dpojet_clr_meas**, clears the measurements.
- **dpojet_state(instr)**, queries the state of the dpojet application.
- **dpojet_run(instr)**, runs the application.
- **dpojet_stop(instr)**, stops the application.
- **dpojet_population(instr,n)**, sets the population.
- **def dpojet_period(instr)**, sets the time period measurement.
- **def dpojet_result(instr)**, queries the measured values.
- **dpojet_status_query(instr)**, queries the status of measurement.
- **dpojet_quickset(instr,n)**, configures and measures the jitter in time period.

