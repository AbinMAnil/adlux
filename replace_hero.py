import sys

with open('desktop_code.html', 'r') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if '<!-- Hero Section -->' in line:
        start_idx = i
    if '<!-- About Us / Expertise -->' in line:
        end_idx = i
        break

new_hero = """<!-- Hero Section -->
<section class="relative pt-32 pb-16 overflow-hidden bg-surface">
<div class="max-w-container-max mx-auto px-gutter">
    
    <!-- Top Row: Headline & Left Elements -->
    <div class="flex flex-col md:flex-row items-center md:items-start gap-8 md:gap-16 mb-16">
      
      <!-- Left side (Avatars & Learn More) -->
      <div class="flex flex-col gap-12 md:w-1/4 pt-6 hidden md:flex">
        <div class="flex items-center gap-6">
          <div class="grid grid-cols-2 gap-2 w-16">
            <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuABfhhjrRsbt6mzXL6enxZmN8tPsG4B4x3KTugrc5G1GOV_eklBO6Ri9PuHPUalhUpJ60EX7VPQrc4d4x9np4jCWT2FcRutI95R45S0EzjQzDh1EpyL1vpx9GnC7SE0vNOSPXg41-XmX6TPB74RiWzIc9BKjCauwZJrmPa85jPIbjXwceWvRes3We7ce8aCuKcBVTlG8ra8LRcQWPZWUG9CtDoYb35jmzUgdSHHpeJZScx9g13eMo8yWofpXtW_g9Hntnu4jqJvzlU" class="w-7 h-7 rounded-full object-cover">
            <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuA96gDrZSc4qLZFT7n_nQp5PDR1xl6YbW092ILW0VjCKvR8WeOLYK3JXWSLhC0i8BiRcb_gQ833ewBnL-U2-2iT65kmHDhh3yXG7hY4j-Oxi4yGCC8UbYQdxHWJLpalvigyicBkLJXb06dt7POaMaVaeMiO3YG8HJQg9Bz828WAZUhw9z942a9E_3HPU0mYBpk0CCcAM9-6aZDXbPSD3IQquU1_rV5eR5jsVOM5i9ku355_gR6jsOS7hFGOf9aBbsMFchu-ay3FPRA" class="w-7 h-7 rounded-full object-cover">
            <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuCO36ZK2Bi9x-hmpeFmMPfWM0MnOS6GZjviqiuOJ-5h55x-oQ_rlX4gX8BNcNJk0v_WI4qeUz-PmBbIiN1TYOQM-xwpCX-2EnBc76LyRSJ9e0b8SjuYharTm2_eU61vnPwH-FlhmrzNhps60dOsvSiImUuStK_uuRtY7FKOimk7wBrQ1VOpU4Ov3AScfgcE-I7hODIj6Scq6p1T8JnbiEdLMWeqJ8i4uC34cyJEvTX048gU9xak0yX8-XUqacfjIL4ovCyAxd672AI" class="w-7 h-7 rounded-full object-cover">
            <div class="w-7 h-7 rounded-full bg-primary flex items-center justify-center text-white text-[12px] font-bold">+</div>
          </div>
          <!-- Dots -->
          <div class="flex flex-col gap-1.5">
            <div class="w-1.5 h-1.5 rounded-full bg-surface-variant"></div>
            <div class="w-1.5 h-1.5 rounded-full bg-surface-variant"></div>
            <div class="w-1.5 h-1.5 rounded-full bg-on-surface"></div>
          </div>
        </div>
        
        <div class="flex items-center text-on-surface hover:text-primary transition-colors group cursor-pointer w-max relative">
          <span class="material-symbols-outlined font-light text-3xl group-hover:translate-x-2 transition-transform absolute -left-8 text-on-surface-variant">arrow_right_alt</span>
          <span class="text-label-md border border-glass-stroke rounded-full px-6 py-2 glassmorphism inline-block ml-4">Learn More</span>
        </div>
      </div>
      
      <!-- Headline -->
      <div class="md:w-3/4 text-center md:text-left">
        <h1 class="text-5xl md:text-7xl lg:text-[5.5rem] font-headline-lg font-light italic text-on-surface tracking-tight leading-[1.2]">
          Beyond the Pill, Your <br/>
          Caring Pharmacy
          <span class="inline-block align-middle ml-2 md:ml-4 w-20 md:w-32 h-10 md:h-16 rounded-[2rem] overflow-hidden border border-glass-stroke soft-shadow bg-mint-green/20">
             <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuCXO1xEwOHsb304hw9LVyxiMM44BPZDvt-NTm-7Itvjh_x6Y_gMW400i4atJOKcB256VHvvrpsLHPlDzAZ--MSCGSRw39QDrYAB6a5Wr3JH277eDQMoHrqqvg9CCi6sFHvZv58dYTP5Au0Xho5eRsLmPV7jrYl1vraCPth8PUjRzCJGTPS9VPbN48oAlrrLoV4oi6csEl7PaEEa36ZPBKHJ6Krx8mhmOFUvp26lRWuo6a3GAewoM9vFc5TrNdrEGzcq3NfQYgAO8jo" class="w-full h-full object-cover mix-blend-multiply opacity-80"/>
          </span>
        </h1>
      </div>
    </div>
    
    <!-- Partner Logos -->
    <div class="flex flex-wrap justify-center md:justify-between items-center gap-6 md:gap-4 opacity-40 grayscale hover:grayscale-0 transition-all duration-500 mb-16 px-4">
      <span class="font-headline-md text-xl tracking-widest font-bold">Niscala.io</span>
      <span class="font-headline-md text-xl tracking-widest font-bold">SAMTIV</span>
      <div class="flex items-center gap-1"><span class="material-symbols-outlined">ac_unit</span><span class="font-headline-md text-xl tracking-widest font-bold">IEA.</span></div>
      <span class="font-headline-md text-xl tracking-widest font-bold">SLAVA</span>
      <span class="font-headline-md text-xl tracking-widest font-bold flex items-center gap-1"><span class="material-symbols-outlined text-[16px]">diamond</span>UNICA</span>
      <span class="font-headline-md text-xl tracking-widest font-bold border-l-4 border-current pl-2">BOKING</span>
    </div>

    <!-- Bottom Row: Image + Text block -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-12">
      
      <!-- Left side (Image & Cards) -->
      <div class="lg:col-span-2 relative rounded-[2rem] overflow-hidden bg-mint-green/20 min-h-[300px] md:min-h-[400px]">
        <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuCXO1xEwOHsb304hw9LVyxiMM44BPZDvt-NTm-7Itvjh_x6Y_gMW400i4atJOKcB256VHvvrpsLHPlDzAZ--MSCGSRw39QDrYAB6a5Wr3JH277eDQMoHrqqvg9CCi6sFHvZv58dYTP5Au0Xho5eRsLmPV7jrYl1vraCPth8PUjRzCJGTPS9VPbN48oAlrrLoV4oi6csEl7PaEEa36ZPBKHJ6Krx8mhmOFUvp26lRWuo6a3GAewoM9vFc5TrNdrEGzcq3NfQYgAO8jo" class="absolute inset-0 w-full h-full object-cover mix-blend-multiply opacity-50"/>
        
        <!-- Floating Card 1 -->
        <div class="absolute bottom-8 left-4 md:left-12 glassmorphism p-5 rounded-[1.5rem] flex flex-col gap-5 soft-shadow bg-white w-[220px] md:w-[260px]">
          <div class="flex gap-4">
             <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuA96gDrZSc4qLZFT7n_nQp5PDR1xl6YbW092ILW0VjCKvR8WeOLYK3JXWSLhC0i8BiRcb_gQ833ewBnL-U2-2iT65kmHDhh3yXG7hY4j-Oxi4yGCC8UbYQdxHWJLpalvigyicBkLJXb06dt7POaMaVaeMiO3YG8HJQg9Bz828WAZUhw9z942a9E_3HPU0mYBpk0CCcAM9-6aZDXbPSD3IQquU1_rV5eR5jsVOM5i9ku355_gR6jsOS7hFGOf9aBbsMFchu-ay3FPRA" class="w-14 h-14 md:w-16 md:h-16 rounded-xl object-cover"/>
             <div>
               <h4 class="font-headline-md text-sm md:text-label-md text-on-surface font-bold">Dr. Wasly Morgan</h4>
               <p class="text-[11px] md:text-[12px] text-on-surface-variant">Cardiologist</p>
               <div class="flex gap-2 md:gap-4 mt-2 text-[10px] md:text-[11px] text-on-surface-variant">
                 <div><span class="font-bold text-on-surface">15y</span> Exp.</div>
                 <div><span class="font-bold text-on-surface">1,548</span> Patient</div>
               </div>
             </div>
          </div>
          <div class="flex justify-between items-center w-full">
             <div class="flex gap-2">
                <div class="w-6 h-6 rounded-full bg-red-50 text-red-400 flex items-center justify-center"><span class="material-symbols-outlined text-[14px]">favorite</span></div>
                <div class="w-6 h-6 rounded-full bg-blue-50 text-blue-400 flex items-center justify-center"><span class="material-symbols-outlined text-[14px]">water_drop</span></div>
                <div class="w-6 h-6 rounded-full bg-purple-50 text-purple-400 flex items-center justify-center"><span class="material-symbols-outlined text-[14px]">star</span></div>
             </div>
             <span class="material-symbols-outlined text-on-surface-variant font-light">arrow_right_alt</span>
          </div>
        </div>
        
        <!-- Floating Card 2 -->
        <div class="absolute top-1/2 right-4 md:right-12 -translate-y-1/2 glassmorphism p-5 rounded-[1.5rem] flex flex-col gap-5 soft-shadow bg-white w-[220px] md:w-[260px] hidden sm:flex">
          <div class="flex gap-4">
             <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuA4mi_imjpBswdZjBGKLsIygPKKqc-tVuGUDIJD-WM4_Pr3jAhZQX38VrPm-07JYic5R-1GaclfAR27ZUyZK_PWAzotH0HI2T8A80B5k9gyRtOJXpUNirV2NAb3mXmVMTXWmR1zqsToMggZ3Tc6Ru0izIT8dCX4juoX2B1jtmUKvSpBywyJKODsUAGouripv9903YT-80_xJGFgqfhAQzN9nfB4qwWIk9zYSwJ0HeG5Y-XW9C2jxs-wAgM-O8n7LzeIpnLiy0blOl8" class="w-14 h-14 md:w-16 md:h-16 rounded-xl object-cover"/>
             <div>
               <h4 class="font-headline-md text-sm md:text-label-md text-on-surface font-bold">Dr. Michael Thompson</h4>
               <p class="text-[11px] md:text-[12px] text-on-surface-variant">Oncologist</p>
               <div class="flex gap-2 md:gap-4 mt-2 text-[10px] md:text-[11px] text-on-surface-variant">
                 <div><span class="font-bold text-on-surface">20y</span> Exp.</div>
                 <div><span class="font-bold text-on-surface">3,948</span> Patient</div>
               </div>
             </div>
          </div>
          <div class="flex justify-between items-center w-full">
             <div class="flex gap-2">
                <div class="w-6 h-6 rounded-full bg-blue-50 text-blue-400 flex items-center justify-center"><span class="material-symbols-outlined text-[14px]">person</span></div>
                <div class="w-6 h-6 rounded-full bg-yellow-50 text-yellow-500 flex items-center justify-center"><span class="material-symbols-outlined text-[14px]">star</span></div>
                <div class="w-6 h-6 rounded-full bg-red-50 text-red-400 flex items-center justify-center"><span class="material-symbols-outlined text-[14px]">favorite</span></div>
             </div>
             <span class="material-symbols-outlined text-on-surface-variant font-light">arrow_right_alt</span>
          </div>
        </div>
      </div>
      
      <!-- Right side (Info & Navigation) -->
      <div class="flex flex-col justify-between py-4 gap-8">
        
        <div>
            <!-- Top Icons -->
            <div class="flex justify-between items-start mb-8">
              <div class="flex gap-3">
                <div class="w-10 h-10 rounded-full bg-red-50 text-red-500 flex items-center justify-center soft-shadow"><span class="material-symbols-outlined text-[20px]">monitor_heart</span></div>
                <div class="w-10 h-10 rounded-full bg-blue-50 text-blue-500 flex items-center justify-center soft-shadow"><span class="material-symbols-outlined text-[20px]">pill</span></div>
                <div class="w-10 h-10 rounded-full bg-purple-50 text-purple-500 flex items-center justify-center soft-shadow"><span class="material-symbols-outlined text-[20px]">biotech</span></div>
              </div>
              <div class="font-headline-md font-bold text-xl text-on-surface">
                01<span class="text-sm text-on-surface-variant font-normal">/05</span>
              </div>
            </div>
            
            <!-- Paragraph -->
            <p class="text-[14px] text-on-surface-variant leading-relaxed">
              Our service goes beyond just providing medication. We offer holistic health solutions, including advice and support, to enhance your quality of life and overall wellness.
            </p>
        </div>
        
        <!-- Bottom CTA -->
        <div class="flex items-center justify-between">
          <h3 class="font-headline-lg text-3xl font-medium max-w-[180px] leading-tight text-on-surface">Health in Every <br/> Dose</h3>
          <button class="w-14 h-14 rounded-full bg-white border border-glass-stroke soft-shadow flex items-center justify-center text-on-surface hover:bg-primary hover:text-white transition-colors cursor-pointer">
            <span class="material-symbols-outlined">chevron_right</span>
          </button>
        </div>
      </div>
      
    </div>
  </div>
</section>
"""

if start_idx != -1 and end_idx != -1:
    new_lines = lines[:start_idx] + [new_hero] + lines[end_idx:]
    with open('desktop_code.html', 'w') as f:
        f.writelines(new_lines)
    print("Replaced desktop successfully")

with open('mobile_code.html', 'r') as f:
    lines_m = f.readlines()

start_idx_m = -1
end_idx_m = -1
for i, line in enumerate(lines_m):
    if '<!-- Hero Section -->' in line:
        start_idx_m = i
    if '<!-- Expertise Section (Bento Grid) -->' in line:
        end_idx_m = i
        break

if start_idx_m != -1 and end_idx_m != -1:
    new_lines_m = lines_m[:start_idx_m] + [new_hero] + lines_m[end_idx_m:]
    with open('mobile_code.html', 'w') as f:
        f.writelines(new_lines_m)
    print("Replaced mobile successfully")

