import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

# Read inventory and extracted data
with open('data/portfolio-inventory.json', 'r', encoding='utf-8') as f:
    inventory = json.load(f)

with open('data/extracted-content.json', 'r', encoding='utf-8') as f:
    extracted = json.load(f)

# Define rich project definitions
projects_metadata = {
    "al_saif": {
        "id": "al_saif",
        "title": {
            "en": "Al-Saif Real Estate Development",
            "ar": "شركة السيف للتطوير العقاري"
        },
        "category": {
            "id": "real_estate",
            "en": "Real Estate & Architecture",
            "ar": "العقارات والتطوير العقاري"
        },
        "tagline": {
            "en": "Retro Vintage Advertising, Direct Sales Strategy & Strategic Content Plans",
            "ar": "إعلانات ريترو التمانينات، حملات البيع المباشر وخطط المحتوى الاستراتيجي"
        },
        "description": {
            "en": "A multi-phase real estate marketing campaign across East and West Beni Suef for Al-Saif Developments. Features the iconic retro advertising campaign ('From East to West Nile... Al-Saif Knows Where to Build'), strategic content plans for Al-Rawda Towers and University Tower, and direct response sales funnels with transparent price-per-meter positioning.",
            "ar": "حملة تسويقية متكاملة متعددة المراحل لمشاريع شركة السيف للتطوير العقاري بشرق وغرب بني سويف. تتضمن الحملة الإعلانية الشهيرة بنمط ريترو التمانينات ('من شرق النيل لغربه... السيف تعرف تختار المكان')، وخطط محتوى استراتيجية لأبراج الروضة وبرج الجامعة، وحملات بيع مباشر فورية واستثمارية بقيم واضحة."
        },
        "tools": ["Content Planning", "Copywriting", "Creative Direction", "Excel", "Retro Advertising", "Photoshop"],
        "featured": True,
        "badge": {"en": "Direct Sales & Retro Campaign", "ar": "بيع مباشر وحملة ريترو"},
        "coverImage": "Nada_Portfolio/Nada_Portfolio/01_Content_Plans/السيف/السيف.1 (4).png",
        "highlights": {
            "en": ["Retro 80s Beni Suef Campaign", "Al-Rawda Towers Sold-Out Phase 1 Strategy", "East & West Nile Strategic Positioning", "Immediate & Off-Plan Sales Messaging"],
            "ar": ["حملة ريترو التمانينات لبني سويف", "استراتيجية الإعلان عن اكتمال بيع البرج الأول بأبراج الروضة", "التموضع الاستراتيجي لشرق وغرب النيل", "رسائل بيعية للوحدات الفورية وتحت الإنشاء"]
        }
    },
    "al_mansour_6": {
        "id": "al_mansour_6",
        "title": {
            "en": "Al-Mansour Developments — 6th Anniversary Campaign",
            "ar": "شركة المنصور للتطوير — كامبين الذكرى السادسة"
        },
        "category": {
            "id": "campaigns",
            "en": "360° Brand Campaigns",
            "ar": "الحملات الإعلانية الشاملة"
        },
        "tagline": {
            "en": "Flagship 360° Brand Campaign: 'From the First Dream... Until It Becomes a Place'",
            "ar": "الحملة الكبرى للذكرى السادسة: 'من أول حلم... لحد ما يبقى مكان'"
        },
        "description": {
            "en": "A comprehensive 6th-anniversary brand celebration for Al-Mansour Developments. Spanning a 22-page master campaign deck, cinematic video production script, full video execution, and multi-format social media calendar depicting a heartwarming father-son architectural heritage story.",
            "ar": "حملة متكاملة للذكرى السنوية السادسة لشركة المنصور للتطوير العقاري. تشمل بريزينتيشن استراتيجي شامل من 22 صفحة، سكريبت إعلاني سينمائي يربط بين حلم الأب المهندس المعماري وابنه، فيديو إعلاني منفذ بالكامل، وجدول نشر منشورات تفاعلية تعزز الثقة والانتماء."
        },
        "tools": ["Campaign Ideation", "Video Scriptwriting", "Cinematic Direction", "Deck Architecture", "ODS / Calc", "Video Editing"],
        "featured": True,
        "badge": {"en": "22-Page Master Deck & Video", "ar": "بريزينتيشن 22 صفحة وفيديو إعلاني"},
        "coverImage": "Nada_Portfolio/Nada_Portfolio/02_Campaigns/campaign El Mansour 6/campaign El Mansour 6 posts/المنصور.1 (1).png",
        "videoPath": "Nada_Portfolio/Nada_Portfolio/02_Campaigns/campaign El Mansour 6/campaign El Mansour 6 video/16_mansory (1).mp4",
        "highlights": {
            "en": ["22-page Strategic Campaign Presentation", "Cinematic Storytelling (Father & Son Legacy)", "Omnichannel Social Media Launch", "Complete High-Def Video Production"],
            "ar": ["عرض تقديمي استراتيجي من 22 صفحة", "سرد قصصي سينمائي (إرث الأب والابن المعماري)", "إطلاق رقمي متعدد القنوات", "إنتاج فيديو إعلاني عالي الجودة"]
        }
    },
    "scientific_center_designs": {
        "id": "scientific_center_designs",
        "title": {
            "en": "The Scientific Center — Brand & Course Marketing",
            "ar": "المركز العلمي — التسويق الأكاديمي والهوية البصرية"
        },
        "category": {
            "id": "education",
            "en": "Educational Marketing",
            "ar": "التسويق التعليمي والأكاديمي"
        },
        "tagline": {
            "en": "Complete Marketing Coordination & Visual Creative Assets (114,000+ Views)",
            "ar": "تنسيق تسويقي وإنتاج بصري شامل لكورسات المركز (أكثر من 114,000 مشاهدة)"
        },
        "description": {
            "en": "Full marketing coordination, content creation, and creative visual production for the Scientific Center in Beni Suef. Encompasses over 55 visual design assets, curriculum promotions (AI, Python, Coding, Baccalaureate, Mental Math), event recaps, and video content that achieved approximately 114,000 views.",
            "ar": "إدارة وتنسيق تسويقي متكامل وإنتاج بصري للمركز العلمي ببني سويف. يضم أكثر من 55 تصميماً بصرياً للمناهج التعليمية (الذكاء الاصطناعي، البرمجة، منهج البكالوريا، الحساب الذهني جي ماث)، وتغطيات الأنشطة الطلابية، وفيديوهات ترويجية حققت ما يقارب 114,000 مشاهدة."
        },
        "tools": ["Canva", "Adobe Photoshop", "AI-assisted Design", "Marketing Coordination", "Paid Ads Monitoring", "Creative Concepts"],
        "featured": True,
        "badge": {"en": "55+ Artworks & 114K Views", "ar": "55+ تصميماً و114 ألف مشاهدة"},
        "coverImage": "Nada_Portfolio/Nada_Portfolio/designs/المركز العلمي/لوجو المركز.png",
        "highlights": {
            "en": ["Over 55 Brand & Course Design Artworks", "Achieved ~114,000 Verified Video Views", "Multi-discipline Curriculum Campaigns", "Audience Geographic & Performance Analysis"],
            "ar": ["أكثر من 55 تصميماً إبداعياً للمركز والكورسات", "تحقيق قرابة 114,000 مشاهدة موثقة", "حملات متنوعة للبرمجة والذكاء الاصطناعي والبكالوريا", "تحليل التوزيع الجغرافي للجمهور ونتائج الإعلانات"]
        }
    },
    "video_production": {
        "id": "video_production",
        "title": {
            "en": "Video Scriptwriting & Production Direction",
            "ar": "اسكريبتات الفيديو والإخراج الإبداعي"
        },
        "category": {
            "id": "video_production",
            "en": "Video Scriptwriting & Production",
            "ar": "إخراج واسكريبتات الفيديو"
        },
        "tagline": {
            "en": "Hook-Driven Storytelling, Comedic Tropes & Video Production Coordination",
            "ar": "هوك تشويقي، سرد كوميدي هادف، وإدارة إنتاج متكاملة للفيديو"
        },
        "description": {
            "en": "Screenplays, shot-by-shot hooks, comedic dialogues, and production coordination for high-engagement video assets. Includes the viral Applied AI script ('When you become the family IT department'), the Baccalaureate workshop comedic dialogue, mental math student challenge showcases, and curriculum launch videos.",
            "ar": "كتابة سكريبتات احترافية بمقدمات تشويقية (Hooks) وسيناريوهات كوميدية هادفة، مع إدارة وتنسيق التصوير والإنتاج. يشمل سكريبت كورس الذكاء الاصطناعي التطبيقي ('لما تبقى أنت قسم الـ IT بتاع العيلة كلها')، وسكريبت ورك شوب البكالوريا، وسلسلة تحديات الجي ماث ومنهج البرمجة الجديد."
        },
        "tools": ["Video Scriptwriting", "Production Coordination", "Hook Optimization", "CapCut", "Storyboarding"],
        "featured": True,
        "badge": {"en": "7 Native Videos & 2 Master Scripts", "ar": "7 فيديوهات أصلية وسكريبتات معتمدة"},
        "coverImage": "Nada_Portfolio/Nada_Portfolio/designs/المركز العلمي/ورك شوب البكالوريا.png",
        "highlights": {
            "en": ["Viral 'Family IT Department' AI Script", "Relatable Student Dialogue for Baccalaureate Workshop", "7 Executed MP4 Video Productions in Portfolio", "On-set Production Coordination with Trainers"],
            "ar": ["سكريبت الذكاء الاصطناعي الكوميدي (IT العيلة)", "حوار واقعي فكاهي لورشة عمل البكالوريا", "7 فيديوهات MP4 منفذة بالكامل داخل البورتفوليو", "تنسيق موقع التصوير والمدربين ومتابعة المونتاج"]
        }
    },
    "med_guide": {
        "id": "med_guide",
        "title": {
            "en": "Med Guide Labs — Mystery Teaser Campaign",
            "ar": "معامل ميد جايد — كامبين التحقيق التشويقي"
        },
        "category": {
            "id": "healthcare",
            "en": "Healthcare & Medical",
            "ar": "التسويق الطبي والمعامل"
        },
        "tagline": {
            "en": "Gamified Detective Storytelling: 'Case File #2026 — Something Has Disappeared'",
            "ar": "سرد بوليسي تفاعلي: 'ملف القضية #2026 — في حاجة اختفت... وإحنا بندور عليها'"
        },
        "description": {
            "en": "An innovative medical laboratory teaser campaign framed as a detective investigation. Using crime board evidence, lab tubes, magnifying glasses, torn report clues, and scheduled 48-hour clue drops to build massive suspense and community engagement ahead of the brand reveal.",
            "ar": "كامبين تشويقي غير تقليدي لمعامل تحاليل ميد جايد مصمم بأسلوب تحقيق بوليسي ومسرح جريمة تفاعلي. يعتمد على لوحة أدلة (Evidence Board)، أنابيب عينات، عدسة مكبرة، وقصاصات تقارير ممزقة تسرب أجزاء من العنوان كل 48 ساعة لتشويق الجمهور وتحفيز التفاعل."
        },
        "tools": ["Gamified Content", "Mystery Teaser Strategy", "Copywriting", "Evidence Board Design", "Excel"],
        "featured": True,
        "badge": {"en": "Interactive Detective Campaign", "ar": "حملة تحقيق تفاعلية"},
        "coverImage": "Nada_Portfolio/Nada_Portfolio/02_Campaigns/campaign med guide/معمل ميد جايد تشويق.1 (1).png",
        "highlights": {
            "en": ["Case File #2026 Narrative Arc", "48-Hour Periodic Clue Revealing Mechanism", "Evidence Board Visual Assets", "High Organic Comment & Share Engagement"],
            "ar": ["حبكة سردية لقضية رقم #2026", "نظام نشر ألغاز وأدلة كل 48 ساعة", "تصاميم لوحة أدلة جنائية مبتكرة للمجال الطبي", "تفاعل قياسي من الجمهور لتوقع الحل"]
        }
    },
    "koshary_rashed": {
        "id": "koshary_rashed",
        "title": {
            "en": "Koshary Rashed — Back to School 'Taleb Rashed'",
            "ar": "كشري راشد — كامبين 'طالب راشد' ولجنة إنقاذ الجوع"
        },
        "category": {
            "id": "food_beverage",
            "en": "Food & Beverage Brands",
            "ar": "الأغذية والمطاعم"
        },
        "tagline": {
            "en": "Humorous Student Timetable Transformation & User Challenge Campaign",
            "ar": "تحويل جدول المحاضرات لجدول وجبات وتحديات طلابية مبهجة"
        },
        "description": {
            "en": "A highly relatable back-to-school promotional campaign for Koshary Rashed. Transforms school and university study schedules into culinary timetables ('Class 1: Koshary, Long Lecture: Pasta Casserole, Practical Lab: Dynamite, Finale: Dessert') with the 'Hunger Rescue Committee' UGC contest.",
            "ar": "كامبين تسويقي فكاهي بمناسبة العودة للمدارس والجامعات لمطعم كشري راشد. يعتمد على فكرة 'طالب راشد' و'لجنة إنقاذ الجوع'، حيث يتم تحويل جدول الحصص والمحاضرات إلى جدول وجبات (الحصة الأولى كشري، المحاضرة الطويلة طاجن، العملي ديناميت)، مع مسابقة فيديو لأفضل مواقف الشلة."
        },
        "tools": ["UGC Campaign Strategy", "Youth Tone of Voice", "Creative Copywriting", "Content Calendar", "Excel"],
        "featured": True,
        "badge": {"en": "Back-to-School Viral Concept", "ar": "كامبين عودة الدراسة الفكاهي"},
        "coverImage": "Nada_Portfolio/Nada_Portfolio/02_Campaigns/campaign rashed/Artboard 2 (8).png",
        "highlights": {
            "en": ["'Hunger Rescue Committee' Theme", "Menu items as University Lecture Timetables", "UGC Video Competition for Free Meals", "Tailored to Gen-Z & College Audience"],
            "ar": ["مفهوم 'لجنة إنقاذ الجوع'", "تحويل أصناف المنيو لجدول محاضرات جامعية", "مسابقة تفاعلية بمحتوى يصنعه الطلاب", "نبرة صوت شبابية مرحة ملائمة للجمهور"]
        }
    },
    "platinum": {
        "id": "platinum",
        "title": {
            "en": "Platinum Plus Developments — Luxury Branding",
            "ar": "بلاتنيوم للتطوير العقاري — براندينج وبرج الأوركيد"
        },
        "category": {
            "id": "real_estate",
            "en": "Real Estate & Architecture",
            "ar": "العقارات والتطوير العقاري"
        },
        "tagline": {
            "en": "Architectural Elegance: 'Every Brick Tells the Story of a Choice'",
            "ar": "فخامة معمارية: 'كل طوبة بتحكي عن اختيار'"
        },
        "description": {
            "en": "Comprehensive branding and project launch strategy for Platinum Plus Developments, focusing on Orchid Tower No. 1000. Features retro 80s architectural advertising briefs, premium visual artboards, and structured content calendars emphasizing design excellence and investment value.",
            "ar": "استراتيجية براندينج وتسويق متكاملة لشركة بلاتنيوم بلس للتطوير العقاري وبرج الأوركيد رقم 1000. تشمل كونسيبت إعلانات التمانينات المعمارية ('كل طوبة بتحكي عن اختيار')، تصاميم آرت بورد راقية، وخطط محتوى تركز على القيمة الاستثمارية وجودة التنفيذ."
        },
        "tools": ["Luxury Branding", "Copywriting", "Art Direction", "Excel", "PDF Decks"],
        "featured": False,
        "badge": {"en": "Orchid Tower 1000 & Retro Brief", "ar": "برج الأوركيد 1000 وحملة ريترو"},
        "coverImage": "Nada_Portfolio/Nada_Portfolio/01_Content_Plans/بلاتنيوم/Artboard 1 (8).png",
        "highlights": {
            "en": ["Al-Orchid Tower 1000 Content Calendar", "Branding Strategy Document", "Retro 80s Architecture Concept Brief", "12 High-Resolution Artboards"],
            "ar": ["خطة محتوى برج الأوركيد رقم 1000", "استراتيجية بناء الهوية المؤسسية", "بريف إعلاني بنمط ريترو التمانينات", "12 لوحة تصميم عالية الجودة"]
        }
    },
    "top_land": {
        "id": "top_land",
        "title": {
            "en": "Top Land Towers — 80s Retro Nostalgia Campaign",
            "ar": "أبراج توب لاند — كامبين نوستالجيا التمانينات"
        },
        "category": {
            "id": "real_estate",
            "en": "Real Estate & Architecture",
            "ar": "العقارات والتطوير العقاري"
        },
        "tagline": {
            "en": "'If Top Land Existed in the 80s... Own Your Apartment in Beni Suef'",
            "ar": "'لو توب لاند كانت موجودة في التمانينات... امتلك شقتك في بني سويف'"
        },
        "description": {
            "en": "A nostalgic real estate marketing campaign capitalizing on vintage 80s newspaper textures, navy & gold color palettes, and retro copywriting. Paired with comprehensive residential tower content schedules for Beni Suef prime locations.",
            "ar": "كامبين عقاري مبتكر يعيد إحياء نوستالجيا إعلانات الصحف في الثمانينات بألوان الكحلي والذهبي والخطوط الكلاسيكية ('لو توب لاند كانت موجودة في التمانينات... كانوا هيقولوا لك امتلك شقتك في بني سويف قبل ما الأسعار تسبقك')، مع خطة محتوى متكاملة و17 تصميماً معمارياً."
        },
        "tools": ["Retro Copywriting", "Graphic Texture Direction", "Content Calendar", "Excel", "Word"],
        "featured": False,
        "badge": {"en": "17 Designs & 80s Trend Brief", "ar": "17 تصميماً وبريف ترند التمانينات"},
        "coverImage": "Nada_Portfolio/Nada_Portfolio/01_Content_Plans/توب لاند/ترند التمنينات.توب لاند.png",
        "highlights": {
            "en": ["Retro 80s Beni Suef Real Estate Concept", "17 Render & Architectural Design Artboards", "Complete Social Media Monthly Calendar", "Flexible Installment Positioning"],
            "ar": ["كونسيبت إعلانات الثمانينات لبني سويف", "17 تصميماً معمارياً ورندرات سكنية", "خطة نشر شهرية شاملة على إكسيل", "صياغة عروض التقسيط والاستلام"]
        }
    },
    "al_zahraa_hospital": {
        "id": "al_zahraa_hospital",
        "title": {
            "en": "Al-Zahraa Hospital — Healthcare & Clinics Marketing",
            "ar": "مستشفى برج الزهراء — التسويق الطبي والعيادات التخصصية"
        },
        "category": {
            "id": "healthcare",
            "en": "Healthcare & Medical",
            "ar": "التسويق الطبي والمعامل"
        },
        "tagline": {
            "en": "Compassionate Medical Communication, Dental Campaigns & Vascular Care",
            "ar": "تواصل طبي إنساني، حملات عيادة الأسنان ومتابعة دوالي الساقين"
        },
        "description": {
            "en": "Strategic multi-clinic communications for Al-Zahraa Tower Hospital. Highlights clinical diagnostic campaigns (such as early varicose vein detection), promotional clinic packages (dental checkups at 50 EGP with 10% procedure discounts), and empathetic medical copywriting across 18 artboards and full October calendars.",
            "ar": "استراتيجية اتصال وتسويق طبي متكامل لمستشفى برج الزهراء. تركز على التوعية التشخيصية لعيادة الأوعية ودوالي الساقين ('رجلك بتوجعك بعد الوقفة؟')، وعروض عيادة الأسنان التشجيعية (كشف بـ 50 جنيه وخصم 10% على العلاجات)، مع 18 تصميماً طبياً وخطة شهر أكتوبر كاملة."
        },
        "tools": ["Healthcare Copywriting", "Patient Education", "Promotional Campaigns", "Excel", "Word"],
        "featured": True,
        "badge": {"en": "18 Medical Artboards & Plans", "ar": "18 لوحة طبية وخطط محتوى"},
        "coverImage": "Nada_Portfolio/Nada_Portfolio/01_Content_Plans/مستشفي الزهراء/Artboard 1 (8).png",
        "highlights": {
            "en": ["Early Varicose Vein Diagnostic Campaign", "Dental Clinic 50 EGP Conversion Offer", "18 High-Quality Healthcare Artboards", "Comprehensive Multi-department Calendar"],
            "ar": ["حملة التوعية بتشخيص دوالي الساقين المبكر", "عرض تحفيزي لكشف الأسنان بـ 50 جنيهاً", "18 لوحة تصميم طبية متخصصة", "خطة محتوى تغطي كافة أقسام المستشفى"]
        }
    },
    "alpha_care": {
        "id": "alpha_care",
        "title": {
            "en": "Alpha Care Laboratories — AI-Assisted Design Masterfiles",
            "ar": "معامل ألفا كير — تصاميم متطورة بالذكاء الاصطناعي وفوتوشوب"
        },
        "category": {
            "id": "creative_design",
            "en": "Creative Design & Branding",
            "ar": "التصميم الإبداعي والهوية"
        },
        "tagline": {
            "en": "23 High-Resolution Adobe Photoshop Masterfiles (PSD) with Layered Assets",
            "ar": "23 ملف فوتوشوب أصلي (PSD) عالي الدقة بمستويات وتفاصيل متقدمة"
        },
        "description": {
            "en": "A sophisticated series of 23 layered Adobe Photoshop masterfiles (PSD) combined with generative AI prompts for Alpha Care medical testing laboratories. Covers health checkup packages, clinical awareness, and futuristic lab branding, fully rendered into instant browser-previewable WebP galleries.",
            "ar": "مجموعة تضم 23 ملف فوتوشوب رئيسي (PSD) متعدد الطبقات، دُمجت فيها أدوات الذكاء الاصطناعي التوليدي مع المعالجة الاحترافية لمعامل ألفا كير للتحاليل الطبية. تشمل باقات الفحص الدوري والتوعية السريرية، ومحولة بالكامل لمعاينات ويب فورية عالية الدقة."
        },
        "tools": ["Adobe Photoshop (PSD)", "Generative AI", "Visual Branding", "Medical Aesthetics", "WebP Optimization"],
        "featured": False,
        "badge": {"en": "23 Layered PSD Masterfiles", "ar": "23 ملف فوتوشوب أصلي PSD"},
        "coverImage": "assets/previews/psd/ChatGPT_Image_Jul_23_2026_10_28_41_PM.webp",
        "highlights": {
            "en": ["23 Full-Resolution Layered PSD Projects", "Direct Browser Previews via Converted WebP", "Prompt Engineering & Generative Healthcare Art", "Original PSD Files Ready for Inspection"],
            "ar": ["23 مشروع فوتوشوب أصلي بكامل الطبقات", "معاينة مباشرة في المتصفح بصيغة WebP فائقة الدقة", "هندسة أوامر الذكاء الاصطناعي للتصميم الطبي", "إمكانية تحميل وفحص ملفات PSD الأصلية"]
        }
    },
    "tameem": {
        "id": "tameem",
        "title": {
            "en": "Tameem Food & Catering — Fayoum District League",
            "ar": "تميم للأغذية — دوري مراكز الفيوم التفاعلي"
        },
        "category": {
            "id": "food_beverage",
            "en": "Food & Beverage Brands",
            "ar": "الأغذية والمطاعم"
        },
        "tagline": {
            "en": "Gamified Regional Competition Deck & Engagement Strategy across Fayoum",
            "ar": "بريزينتيشن مسابقة تنافسية بين مراكز الفيوم واستراتيجية تفاعل حماسية"
        },
        "description": {
            "en": "A gamified regional competition campaign for Tameem across Fayoum governorate. Centers around an 8-page master competition strategy deck pitting districts (Al-Nazlah vs Al-Agameen vs Abu Gansho vs Al-Nasriyah vs Abu Kasah) against each other with order-based voting.",
            "ar": "حملة تنافسية تسويقية مبتكرة لعلامة تميم الغذائية في محافظة الفيوم. تتمحور حول بريزينتيشن استراتيجي من 8 صفحات ينظم مسابقة حماسية بين مراكز الفيوم (النزلة، العجميين، أبو جنشو، النصرية، أبو كساه)، حيث يدعم كل طلب توصيل فرصة المركز في الفوز بجوائز ضخمة."
        },
        "tools": ["Gamified Campaign Strategy", "PDF Presentation Deck", "Community Marketing", "ODS / Calc", "Artboards"],
        "featured": False,
        "badge": {"en": "8-Page Deck & District League", "ar": "عرض 8 صفحات ودوري تنافسي"},
        "coverImage": "Nada_Portfolio/Nada_Portfolio/02_Campaigns/campaign tameem/Artboard 1..png",
        "highlights": {
            "en": ["8-page Regional Tournament Master Deck", "Fayoum District Gamification Mechanics", "6 Custom Social Artboards", "Direct Data Table & Order Tracking Matrix"],
            "ar": ["عرض تقديمي للمسابقة من 8 صفحات", "آلية تنافسية مناطقية مبتكرة لأهل الفيوم", "6 لوحات تصميم حصرية للحملة", "جدول تتبع البيانات واحتساب النتائج"]
        }
    },
    "dr_mulla": {
        "id": "dr_mulla",
        "title": {
            "en": "Dr. Al-Mulla Clinic — Specialized Medical Content",
            "ar": "عيادة د. الملا — المحتوى الطبي التخصصي"
        },
        "category": {
            "id": "healthcare",
            "en": "Healthcare & Medical",
            "ar": "التسويق الطبي والمعامل"
        },
        "tagline": {
            "en": "Strategic September Healthcare Calendar & Educational Artboards",
            "ar": "خطة محتوى شهر سبتمبر الطبية ولوحات توعوية للمرضى"
        },
        "description": {
            "en": "A specialized monthly medical social media plan for Dr. Al-Mulla. Features 8 dedicated medical artboards and a detailed September content schedule addressing patient inquiries, medical advice, and clinic scheduling.",
            "ar": "خطة تسويق ونشر شهرية لعيادة د. الملا الطبية. تتضمن 8 تصاميم توعوية متخصصة وجدول إكسيل لشهر سبتمبر يتناول الإرشادات الصحية الموثوقة، وتسهيل حجز المواعيد والاستشارات."
        },
        "tools": ["Medical Social Content", "Content Planning", "Excel", "Design Artboards"],
        "featured": False,
        "badge": {"en": "8 Artboards & September Plan", "ar": "8 تصاميم وخطة شهر سبتمبر"},
        "coverImage": "Nada_Portfolio/Nada_Portfolio/01_Content_Plans/د.الملا/Artboard 1 (8).png",
        "highlights": {
            "en": ["8 Custom Clinic Artboards", "September Content Schedule Spreadsheet", "Clear Patient Call-to-Action", "Specialized Healthcare Communication"],
            "ar": ["8 لوحات تصميم مخصصة للعيادة", "جدول إكسيل منظم لشهر سبتمبر", "دعوات تواصل وحجز واضحة", "أسلوب تواصل طبي مبسط وموثوق"]
        }
    },
    "dr_hady": {
        "id": "dr_hady",
        "title": {
            "en": "Dr. Hady Clinic — Clinical Advisory & Content Plan",
            "ar": "عيادة د. هادي — الإرشادات السريرية وخطة المحتوى"
        },
        "category": {
            "id": "healthcare",
            "en": "Healthcare & Medical",
            "ar": "التسويق الطبي والمعامل"
        },
        "tagline": {
            "en": "Patient Trust Building, Preventive Care & Structured Social Schedule",
            "ar": "بناء ثقة المرضى، التوعية الوقائية وجدول نشر منظم"
        },
        "description": {
            "en": "Professional clinical communication plan for Dr. Hady clinic. Features 5 branded visual artworks and an interactive Excel content schedule providing actionable medical tips and clinic appointment coordination.",
            "ar": "خطة تواصل سريري متخصصة لعيادة د. هادي. تشمل 5 تصاميم بصرية مميزة وجدول محتوى تفاعلي يقدم نصائح وقائية هامة ويسهل حجز الكشف والمتابعة."
        },
        "tools": ["Clinical Copywriting", "Content Planning", "Excel", "Art Direction"],
        "featured": False,
        "badge": {"en": "5 Artboards & Dedicated Plan", "ar": "5 تصاميم وخطة مخصصة"},
        "coverImage": "Nada_Portfolio/Nada_Portfolio/01_Content_Plans/د.هادي/Artboard 10 (3).png",
        "highlights": {
            "en": ["5 Medical Visual Artboards", "Interactive Content Spreadsheet", "Preventive Care Guidance", "Consistent Clinic Brand Tone"],
            "ar": ["5 لوحات تصميم طبية مميزة", "جدول محتوى تفاعلي منظم", "إرشادات طبية وقائية دورية", "نبرة صوت موثوقة تعزز الاطمئنان"]
        }
    },
    "egyptian_saudi_center": {
        "id": "egyptian_saudi_center",
        "title": {
            "en": "Egyptian Saudi Center — Educational Consultancy",
            "ar": "المركز المصري السعودي — الاستشارات والبرامج التدريبية"
        },
        "category": {
            "id": "education",
            "en": "Educational Marketing",
            "ar": "التسويق التعليمي والأكاديمي"
        },
        "tagline": {
            "en": "Cross-Border Training Programs, Professional Courses & 17 Design Assets",
            "ar": "برامج تدريبية وتأهيلية مشتركة و17 عملاً وتصميماً بصرياً"
        },
        "description": {
            "en": "Comprehensive educational content strategy for the Egyptian Saudi Center. Includes 17 artboards and visual assets, alongside an extensive Excel content schedule promoting professional diplomas, specialized workshops, and corporate training.",
            "ar": "استراتيجية محتوى متكاملة للمركز المصري السعودي للاستشارات والتدريب. تضم 17 لوحة وتصميماً بصرياً احترافياً، مع جدول نشر إكسيل منظم للتسويق للدبلومات المهنية وورش العمل المتخصصة."
        },
        "tools": ["Consultancy Marketing", "Content Calendar", "Design Artboards", "Excel"],
        "featured": False,
        "badge": {"en": "17 Artboards & Master Plan", "ar": "17 لوحة تصميم وخطة محتوى"},
        "coverImage": "Nada_Portfolio/Nada_Portfolio/01_Content_Plans/المركز المصري السعودي/Artboard 14.png",
        "highlights": {
            "en": ["17 High-Definition Visual Artboards", "Structured Educational Training Calendar", "Professional Diploma Promotions", "Multi-platform Social Strategy"],
            "ar": ["17 لوحة تصميم بصرية عالية الجودة", "جدول إكسيل منظم للبرامج التدريبية", "حملات تسويق الدبلومات المهنية", "استراتيجية نشر متعددة القنوات"]
        }
    },
    "our_retail": {
        "id": "our_retail",
        "title": {
            "en": "OUR Retail & Brand Offers — Conversion Campaigns",
            "ar": "اور للعروض التجارية — حملات العروض والتخفيضات"
        },
        "category": {
            "id": "food_beverage",
            "en": "Food & Beverage Brands",
            "ar": "الأغذية والمطاعم"
        },
        "tagline": {
            "en": "High-Impact Commercial Deals, Seasonal Promotions & Visual Catalogs",
            "ar": "عروض ترويجية مباشرة، تخفيضات موسمية وكتالوج بصري جاذب"
        },
        "description": {
            "en": "Direct response promotional marketing for 'OUR' retail brand. Comprises targeted discount schedules, customer conversion copy, and 5 bold visual promotional artboards.",
            "ar": "حملات تسويقية مباشرة لعلامة 'اور' التجارية. تعتمد على عروض تسعيرية حصرية وخصومات واضحة وجدول إكسيل منظم مع 5 تصاميم بصرية تحفيزية للشراء."
        },
        "tools": ["Promotional Copywriting", "Retail Strategy", "Excel", "Design Layouts"],
        "featured": False,
        "badge": {"en": "5 Promo Artboards & Offers Plan", "ar": "5 تصاميم وخطة العروض"},
        "coverImage": "Nada_Portfolio/Nada_Portfolio/01_Content_Plans/اور/اور8 (1).jpg",
        "highlights": {
            "en": ["5 Commercial Promotion Designs", "Dedicated Offers Spreadsheet", "Conversion-Optimized Copywriting", "Seasonal Clearance Campaigns"],
            "ar": ["5 تصاميم ترويجية لافتة للأنظار", "جدول إكسيل مخصص للعروض والأسعار", "صياغة تحفيزية لسرعة الشراء", "حملات موسمية ومناسبات دورية"]
        }
    },
    "rahhal": {
        "id": "rahhal",
        "title": {
            "en": "Rahhal — Monthly Strategy & Creative Visuals",
            "ar": "رحال — استراتيجية المحتوى والتصاميم البصرية"
        },
        "category": {
            "id": "campaigns",
            "en": "360° Brand Campaigns",
            "ar": "الحملات الإعلانية الشاملة"
        },
        "tagline": {
            "en": "October Strategic Calendar, Visual Branding & Multi-format Artboards",
            "ar": "خطة شهر أكتوبر الاستراتيجية وهوية بصرية متماسكة"
        },
        "description": {
            "en": "Monthly digital marketing strategy and creative visual design for Rahhal. Includes full October schedule with audience engagement mechanics and 6 creative visual layouts.",
            "ar": "استراتيجية تسويق رقمي وإدارة محتوى لعلامة رحال. تشمل جدول شهر أكتوبر المعتمد وآليات تفاعل دورية، مع 6 تصاميم ولوحات بصرية مميزة."
        },
        "tools": ["Brand Strategy", "Content Scheduling", "Excel", "Visual Layouts"],
        "featured": False,
        "badge": {"en": "October Plan & 6 Artworks", "ar": "خطة أكتوبر و6 تصاميم"},
        "coverImage": "Nada_Portfolio/Nada_Portfolio/01_Content_Plans/رحال/3بلان 2.png",
        "highlights": {
            "en": ["October Content Plan Spreadsheet", "6 Branded Visual Layouts", "Engagement-Driven Copywriting", "Coordinated Brand Communication"],
            "ar": ["خطة شهر أكتوبر الكاملة على إكسيل", "6 لوحات وتصاميم بصرية متناسقة", "كابشنز تفاعلية تعزز ولاء العملاء", "تناغم بصري ورسائل واضحة"]
        }
    },
    "al_loloa": {
        "id": "al_loloa",
        "title": {
            "en": "Al-Lo'loa — Content Plan & Social Assets",
            "ar": "اللؤلؤة — خطة المحتوى والأصول الرقمية"
        },
        "category": {
            "id": "campaigns",
            "en": "360° Brand Campaigns",
            "ar": "الحملات الإعلانية الشاملة"
        },
        "tagline": {
            "en": "September Content Strategy, Elegance Positioning & 12 Artboards",
            "ar": "استراتيجية محتوى شهر سبتمبر، تموضع راقٍ و12 لوحة تصميم"
        },
        "description": {
            "en": "Full social media content calendar and aesthetic artboard collection for Al-Lo'loa. Incorporates 12 visual artboards and an Excel planning matrix tailored to brand tone and customer loyalty.",
            "ar": "خطة محتوى متكاملة لشهر سبتمبر ومجموعة تصاميم راقية لعلامة اللؤلؤة. تضم 12 لوحة تصميم مميزة ومصفوفة نشر على إكسيل تعزز نبرة البراند الراقية وثقة الجمهور."
        },
        "tools": ["Content Planning", "Copywriting", "Excel", "Design Artboards"],
        "featured": False,
        "badge": {"en": "12 Artboards & September Matrix", "ar": "12 لوحة وخطة سبتمبر"},
        "coverImage": "Nada_Portfolio/Nada_Portfolio/01_Content_Plans/اللؤلؤه/Artboard 12.png",
        "highlights": {
            "en": ["12 High-Quality Brand Artboards", "September Social Calendar Spreadsheet", "Brand Value & Quality Messaging", "Organized Multi-post Campaign"],
            "ar": ["12 لوحة تصميم إبداعية عالية الجودة", "جدول إكسيل منظم لشهر سبتمبر", "رسائل تركز على الجودة والقيمة", "حملة نشر متسلسلة ومدروسة"]
        }
    },
    "october_greetings": {
        "id": "october_greetings",
        "title": {
            "en": "6th of October — Multi-Brand National Campaigns",
            "ar": "تهنئات نصر أكتوبر — حملات وطنية موحدة للعملاء"
        },
        "category": {
            "id": "campaigns",
            "en": "360° Brand Campaigns",
            "ar": "الحملات الإعلانية الشاملة"
        },
        "tagline": {
            "en": "Cinematic Motion Concepts & Commemorative Designs Across 6 Client Brands",
            "ar": "أفكار فيديو موشن سينمائية وتصاميم وطنية راقية لـ 6 علامات تجارية"
        },
        "description": {
            "en": "A unified national campaign conceptualized and written for multiple client accounts to celebrate 6th of October victory. Spans motion graphic concepts (Sinai sand trace turning into the number 6), motion design PDF briefs, and tailored commemorative artworks for Top Land, Platinum, Al-Mansour, Rahhal, Abu Al-Awam, and Jewelry.",
            "ar": "حملة وطنية موحدة جرى ابتكارها وكتابة نصوصها لعدة علامات تجارية احتفاءً بذكرى نصر أكتوبر المجيد. تتضمن أفكار فيديو موشن جرافيك سينمائية (أثر عبور على رمال سيناء يتحول لرقم 6)، وبريف موشن جرافيك PDF، وتصاميم مخصصة لكل من: توب لاند، بلاتنيوم، المنصور، رحال، أبو العوام، ومجوهرات."
        },
        "tools": ["Motion Concept Ideation", "Creative Copywriting", "Scripting", "PDF Briefs", "Word"],
        "featured": False,
        "badge": {"en": "Motion Concept & 6 Client Artworks", "ar": "فكرة موشن سينمائية وتصاميم لـ 6 عملاء"},
        "coverImage": "Nada_Portfolio/Nada_Portfolio/01_Content_Plans/تهنئات اكتوبر/بلاتنيوم.png",
        "highlights": {
            "en": ["Cinematic Sinai Sand Motion Graphic Concept", "Tailored to 6 Major Brand Accounts", "Commemorative Copywriting & Motion Briefs", "Preserves National Dignity & Brand Identity"],
            "ar": ["فكرة موشن جرافيك مستوحاة من رمال سيناء وعلم مصر", "مخصصة لـ 6 علامات تجارية كبرى", "نصوص وكابشنز وطنية بليغة وبريفات PDF", "توازن مثالي بين الهيبة الوطنية وهوية البراند"]
        }
    },
    "nada_profile": {
        "id": "nada_profile",
        "title": {
            "en": "Nada Nasser Mohamed — Credentials & Official CV",
            "ar": "ندى ناصر محمد — السيرة الذاتية والهوية المهنية"
        },
        "category": {
            "id": "identity",
            "en": "Professional Identity",
            "ar": "الهوية المهنية والخبرات"
        },
        "tagline": {
            "en": "Content Creator | Social Media Specialist | Marketing Coordinator",
            "ar": "صانعة محتوى | أخصائية سوشيال ميديا | منسقة تسويق"
        },
        "description": {
            "en": "Verified professional credentials of Nada Nasser Mohamed. Highlights experience managing content calendars across 24 social media pages, coordination of marketing at the Scientific Center, achieving ~114,000 video views, leadership as Vice President of Rally Society (Beni Suef University), and Faculty of Science education.",
            "ar": "السيرة الذاتية الرسمية والبيانات الموثقة لـ ندى ناصر محمد. توثق خبرتها في إدارة وتخطيط المحتوى لـ 24 صفحة بمختلف المجالات، وتنسيق الأنشطة التسويقية للمركز العلمي، وتحقيق قرابة 114,000 مشاهدة للفيديوهات، ودورها القيادي كنائب رئيس جمعية رالي (جامعة بني سويف)، ودراستها بكلية العلوم."
        },
        "tools": ["Content Planning", "Copywriting", "Social Media Management", "Canva", "Photoshop", "CapCut", "Excel"],
        "featured": True,
        "badge": {"en": "4-Page Verified Official CV", "ar": "سيرة ذاتية موثقة من 4 صفحات"},
        "coverImage": "WhatsApp Image 2026-10-23 at 10.43.44 PM.jpeg",
        "highlights": {
            "en": ["Managed Calendars for 24 Social Pages", "Vice President — Rally Society (BSU)", "Bachelor of Science (Zoology) — Beni Suef University", "Cross-Industry Experience (Real Estate, Medical, Retail, EdTech)"],
            "ar": ["إدارة وتخطيط المحتوى لـ 24 صفحة عميل", "نائب رئيس جمعية رالي بجامعة بني سويف", "بكالوريوس علوم (قسم الحيوان) - جامعة بني سويف", "خبرة متعددة القطاعات (عقارات، طبي، تجاري، تعليمي)"]
        }
    }
}

# Attach files to projects
for proj_id, proj in projects_metadata.items():
    proj["files"] = []

for item in inventory:
    pid = item.get("project_id", "general")
    if pid in projects_metadata:
        projects_metadata[pid]["files"].append(item)

# Build unified JavaScript bundle
js_content = """// ==========================================================================
// Portfolio Master Database - Nada Nasser Mohamed
// Generated automatically from verified files in project repository
// ==========================================================================

window.PORTFOLIO_DATA = {
  profile: {
    name: {
      en: "Nada Nasser Mohamed",
      ar: "ندى ناصر محمد"
    },
    title: {
      en: "Content Creator | Social Media Specialist | Marketing Coordinator",
      ar: "صانعة محتوى | أخصائية سوشيال ميديا | منسقة تسويق"
    },
    location: {
      en: "Beni Suef, Egypt",
      ar: "بني سويف، مصر"
    },
    email: "nada.qotp.uni@gmail.com",
    phone: "01065746707",
    avatar: "WhatsApp Image 2026-10-23 at 10.43.44 PM.jpeg",
    cvPdf: "NADA NASSER MOHAMED con.pdf",
    summary: {
      en: "Results-driven Content Creator, Social Media Specialist, and Marketing Coordinator experienced in managing content calendars across 24 social media pages for diverse clients. Proven track record in campaign ideation, video scriptwriting, coordinating video production with ~114,000 views, visual asset creation, and paid advertising performance monitoring. Leadership experience as Vice President of Rally Society at Beni Suef University.",
      ar: "صانعة محتوى وأخصائية سوشيال ميديا ومنسقة تسويق ذات خبرة عملية في إدارة وتخطيط جداول النشر لأكثر من 24 صفحة عميل عبر مختلف الصناعات. تمتلك سجلاً حافلاً في ابتكار الحملات الإعلانية، كتابة اسكريبتات الفيديو، وتنسيق الإنتاج لفيديوهات حققت نحو 114,000 مشاهدة، بالإضافة لتصميم الأصول البصرية ومتابعة أداء الإعلانات الممولة، مع خبرة قيادية كنائب رئيس جمعية رالي بجامعة بني سويف."
    },
    education: {
      en: "Bachelor of Science — Zoology Department, Faculty of Science, Beni Suef University (Expected Graduation: 2028)",
      ar: "بكالوريوس العلوم — قسم الحيوان، كلية العلوم، جامعة بني سويف (تاريخ التخرج المتوقع: 2028)"
    },
    languages: [
      { name: { en: "Arabic", ar: "العربية" }, level: { en: "Native", ar: "اللغة الأم" } },
      { name: { en: "English", ar: "الإنجليزية" }, level: { en: "Intermediate (B1)", ar: "متوسط (B1)" } }
    ],
    verifiedMetrics: [
      { id: "pages", number: 24, suffix: "+", label: { en: "Social Media Pages Managed", ar: "صفحة عميل تمت إدارتها" } },
      { id: "views", number: 114, suffix: "K+", label: { en: "Verified Video Views", ar: "مشاهدة فيديو موثقة" } },
      { id: "files", number: 265, suffix: "", label: { en: "Original Project Assets", ar: "ملفاً وأصلاً بالبورتفوليو" } },
      { id: "plans", number: 16, suffix: "", label: { en: "Live Content Spreadsheets", ar: "جدول وخطة محتوى تفاعلية" } },
      { id: "videos", number: 7, suffix: "", label: { en: "Produced Video Works", ar: "فيديوهات أصلية منفذة" } },
      { id: "psd", number: 23, suffix: "", label: { en: "Photoshop Masterfiles", ar: "ملف فوتوشوب أصلي" } }
    ],
    experience: [
      {
        role: { en: "Marketing & Content Specialist", ar: "أخصائية تسويق ومحتوى" },
        company: { en: "Scientific Center", ar: "المركز العلمي" },
        location: { en: "Beni Suef, Egypt", ar: "بني سويف، مصر" },
        period: { en: "5 Months", ar: "5 أشهر" },
        points: {
          en: [
            "Coordinated center's marketing activities: content planning, campaign ideation, creative production, and social media operations.",
            "Developed creative marketing concepts, video scripts, and course awareness campaigns.",
            "Produced visual marketing materials using Canva, Adobe Photoshop, and AI-assisted design tools.",
            "Coordinated video production with trainers, achieving ~114,000 video views.",
            "Monitored paid advertising campaigns and reviewed audience geographic distribution."
          ],
          ar: [
            "تنسيق أنشطة المركز التسويقية: تخطيط المحتوى، ابتكار الحملات، الإنتاج الإبداعي، وإدارة السوشيال ميديا.",
            "تطوير أفكار تسويقية مبتكرة، اسكريبتات فيديو، وحملات ترويجية لدعم الوعي بالكورسات.",
            "تصميم مواد تسويقية بصرية باستخدام كانفا وفوتوشوب وأدوات الذكاء الاصطناعي.",
            "إدارة وتنسيق تصوير الفيديوهات مع المدربين، وتحقيق نحو 114,000 مشاهدة.",
            "متابعة أداء الإعلانات الممولة وتحليل التوزيع الجغرافي للمحافظات لاتخاذ قرارات تسويقية مدروسة."
          ]
        }
      },
      {
        role: { en: "Content Creator & Content Planner", ar: "صانعة ومخططة محتوى" },
        company: { en: "Alaa El-Din Company", ar: "شركة علاء الدين" },
        location: { en: "Egypt", ar: "مصر" },
        period: { en: "5 Months", ar: "5 أشهر" },
        points: {
          en: [
            "Managed content planning and publishing schedules across 24 social media pages.",
            "Served clients in real estate, medical laboratories, hospitals, interior finishing, restaurants, and cafés.",
            "Developed tailored content calendars aligned with brand tone, target audience, and promotional objectives.",
            "Wrote social media captions and planned seasonal, occasion-based, and promotional content."
          ],
          ar: [
            "إدارة تخطيط وجداول نشر المحتوى لـ 24 صفحة على منصات التواصل الاجتماعي.",
            "خدمة عملاء بمجالات العقارات، معامل التحاليل، المستشفيات، التشطيبات، المطاعم والكافيهات.",
            "بناء خطط وجداول محتوى مخصصة لكل علامة تجارية وتحديد نبرة الصوت والأهداف البيعية.",
            "كتابة الكابشنز والأفكار الإبداعية للمحتوى الدوري والموسمي والمناسبات الوطنية."
          ]
        }
      },
      {
        role: { en: "Vice President & Former Vice Head of Marketing", ar: "نائب رئيس الجمعية ونائب مسؤول التسويق سابقاً" },
        company: { en: "Rally Society", ar: "جمعية رالي الطلابية" },
        location: { en: "Beni Suef University", ar: "جامعة بني سويف" },
        period: { en: "Present", ar: "حاليًا" },
        points: {
          en: [
            "Contribute to organizational planning, strategic decisions, and execution of student initiatives.",
            "Coordinate with team leaders and members to optimize team performance and member engagement.",
            "Led marketing campaigns and promotional content planning for student recruitment and events."
          ],
          ar: [
            "المساهمة في التخطيط التنظيمي، اتخاذ القرارات، وتنفيذ المبادرات والأنشطة الطلابية.",
            "التنسيق مع قادة الفرق والأعضاء لتعزيز الأداء والمساءلة والعمل الجماعي.",
            "قيادة الحملات التسويقية والترويجية لفعاليات الجمعية ومواسم استقبال الطلاب."
          ]
        }
      }
    ],
    skills: {
      core: [
        { en: "Content Creation & Copywriting", ar: "صناعة المحتوى وكتابة الإعلانات" },
        { en: "Social Media Strategy & Calendars", ar: "استراتيجيات وجداول السوشيال ميديا" },
        { en: "Marketing Campaign Ideation", ar: "ابتكار وتخطيط الحملات الإعلانية" },
        { en: "Video Scriptwriting & Directing", ar: "كتابة اسكريبتات الفيديو والإخراج" },
        { en: "Visual Asset Design & Art Direction", ar: "التصميم الإعلاني والإخراج الفني" },
        { en: "Paid Ads Performance Monitoring", ar: "متابعة أداء وتحليل الإعلانات الممولة" },
        { en: "Audience Geographic Insights", ar: "تحليل رؤى واهتمامات الجمهور الجغرافي" },
        { en: "Team Leadership & Coordination", ar: "القيادة والتنسيق متعدد الوظائف" }
      ],
      tools: [
        "Canva", "Adobe Photoshop", "AI-assisted Design Tools", "CapCut", 
        "Microsoft Excel", "Google Sheets", "Microsoft Word", "Meta Business Suite"
      ]
    }
  },

  categories: [
    { id: "all", en: "All Projects", ar: "جميع المشاريع", icon: "layers" },
    { id: "real_estate", en: "Real Estate & Architecture", ar: "العقارات والتطوير", icon: "building" },
    { id: "campaigns", en: "360° Brand Campaigns", ar: "الحملات الإعلانية", icon: "megaphone" },
    { id: "healthcare", en: "Healthcare & Medical", ar: "التسويق الطبي", icon: "activity" },
    { id: "education", en: "Educational Marketing", ar: "التسويق التعليمي", icon: "graduation-cap" },
    { id: "food_beverage", en: "Food & Beverage", ar: "المطاعم والأغذية", icon: "coffee" },
    { id: "video_production", en: "Video & Scripts", ar: "فيديو واسكريبتات", icon: "video" },
    { id: "creative_design", en: "Creative PSDs & Design", ar: "التصاميم وملفات PSD", icon: "palette" },
    { id: "identity", en: "Credentials & CV", ar: "السيرة الذاتية والخبرات", icon: "user-check" }
  ],

  projects: """ + json.dumps(list(projects_metadata.values()), ensure_ascii=False, indent=2) + """,

  extractedContent: """ + json.dumps(extracted, ensure_ascii=False, indent=2) + """,

  inventory: """ + json.dumps(inventory, ensure_ascii=False, indent=2) + """
};
"""

with open('data/portfolio-database.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Generated data/portfolio-database.js successfully!")
print(f"File size: {os.path.getsize('data/portfolio-database.js')} bytes")
