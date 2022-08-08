import random
kelimeler = ["gözəl ","məlumat ","sual","sağlam ","buraxmaq","yaraşıqlı","su","etmək","işlədmək","demək","görmək",
             "yenidən", "həssas", "sanki", "manat", "oynamaq", "çiçək", "şəhər", "yüksəlmək", "çabalamaq", "varlıq", "diyar",
             "güvən", "gərək", "müalicə", "bir", "rahat", "soyuq", "hava", "kitab", "paylaşmaq", "hesap", "vücud",
             "torpaq", "kitab", "sistem", "xoşallanmaq", "çəkilmək", "texnik", "yaxınlaşmaq", "il", "tarix", "dəqiq", "qaqaş",
             "nazik", "dəyər", "orda", "qarşılıq","vermək", "sahib", "artıq", "kişi", "digər", "dönmək", "yenə", "enlikürək",
             "dəftər", "hadisə", "tapmaq", "göz", "dövlət", "qabağ", "tələb", "baxmaq", "üstündə", "belə", "bəzi", "başlamaq",
             "tutmaq", "birə", "heç", "göstərmək", "hovuz", "kimi", "hal", "doğru", "orta", "başqa", "böyük", "getmək",
             "yeni", "çox", "soruşmaq", "onlar", "açmaq", "dəniz", "həmişə", "səs", "anlamaq", "dəli", "saat", "neçə",
             'aydın', 'və', 'aparmaq', 'bu', 'üçün', 'sevgi', 'qığılcım', 'demək', 'delfin', 'maral', 'nə', 'balıq', 'daha', 'almaq',
             'var', 'kənd', 'qonaq', 'ildə', 'mənim', 'ancaq', 'sonra', 'qismət', 'yer', 'məhəbbət', 'insan', 'sənsiz', 'dalğalı',
             'istəmək', 'yubley', 'çıxmaq', 'görmək', 'gün', 'bizim', 'zalım', 'iş', 'ara', 'məsafə', 'lakin', 'bilmək', 'elçi', 'həyat',
             'yazmaq', 'uşaq', 'iki', 'baxmaq', 'çalışmaq', 'sevda', 'böyük', 'yox', 'bitirmək', 'yol', 'qalmaq', 'nədən', 'yolçu',
             'söhbət', 'dalğalı', 'yaxşı', 'qadın', 'ev', 'ordu', 'axtarmaq', 'susmaq', 'söz', 'önəmli', 'dünya',
             'baş', 'status', 'yan', 'keçmək', 'sən', 'qoyun', 'təzə', 'əvvəlcə', 'başqa', 'telefon', 'məxrəc', 'çay', 'girmək', 'ölkə',
             'yemək', 'qaş', 'oba', 'işıq', 'bütün', 'qarşı', 'tapmaq', 'qələm', 'yaşamaq', 'düşünmək', 'eyni', 'iç', 'dərya',
             'ər', 'qabıq', 'gözləmək', 'ilk', 'burun', 'başlanğıc', 'son', 'çətin', 'şəkil', 'vacib', 'yüz', 'yağış', 'görmək', 'gündüz',
             'alt', 'gətirmək', 'işçi', 'çünki', 'tərəf', 'indi', 'adam', 'onun', 'qar', 'əks', 'qapı', 'səs', 'həmkar',
             'doğru', 'durmaq', 'qız', 'bütün', 'çəkmək', 'danışmaq', 'pul', 'düşmək', 'ata', 'az', 'bəzi', 'baba', 'hayat',
             'sadəcə
             ', 'kiçik', 'yüksəlmək', 'ağartı', 'ay', 'akvarium', 'açar', 'sevmək', 'yenə', 'sağlamaq', 'nəticə', 'istifadəçi', 'çöl',
             'ad', 'məsələ', 'saniyə', 'döndərmək', 'açmaq', 'oturmaq', 'gül', 'qol', 'dəqiqə', 'saat', 'yaş', 'problem', 'ağac',
             'sahil', 'sıra', 'cərgə', 'hasar', 'gündəlik', 'atmaq', 'tutmaq', 'diş', 'tərcümə', 'qaçmaq', 'yorğun', 'reklam', 'misal',
             'qum', 'biraz', 'zor', 'biləsuvar', 'bu', 'tənha', 'tək', 'sistem', 'birlikdə', 'dul', 'nömrə', 'aldanmaq', 'gənc',
             'qan', 'darağ', 'maşın', 'tıncıxmaq', 'gecə', 'xəritə', 'bizon', 'şifrə', 'donmaq', 'uzun', 'maska', 'saç', 'yas',
             'dost', 'çeşid', 'ailə', 'şar', 'oxumaq', 'balon', 'əqrəb', 'güc', 'balina', 'dürüst', 'kalonka', 'əlaqə', 'münasibət',
             'ətraf', 'köhnə', 'kifayət', 'müsəlman', 'cümlə', 'kənar', 'küçə', 'bəy', 'sarı', 'kəsmək', 'seriya', 'şəxsi', 'ağıl',
             'səssiz', 'pak', 'əymək', 'gərək', 'ayrılıq', 'məna', 'yüksək', 'bank', 'gəlin', 'sıra', 'daşımaq', 'geri', 'toplanmaq',
             'nardaran', 'maddə', 'məhsul', 'qərar', 'kor', 'yağlamaq', 'saymaq', 'fərqli', 'qrup', 'otağ', 'bildirçin', 'kanal', 'xəbər',
             'sürmək', 'xına', 'gələcək', 'millət', 'soğan', 'arxa', 'qazanmaq', 'yazı', 'dərs', 'açıq', 'öyrənmək', 'qəza',
             'dil', 'şirkət', 'qaynaq', 'bitki', 'program', 'davam', 'sürüşmək', 'reng', 'müəllim', 'haqq', 'inanmaq',
             'dərslik', 'acı', 'parça', 'qəzet', 'bərbər', 'təbib', 'toxunmaq', 'tanımaq', 'kredit', 'həkim', 'maaş',
             'vəzifə', 'məqsəd', 'bölgə', 'film', 'dayı', 'köçmək', 'haqqında', 'qayıtmaq', 'lezva', 'kür', 'ikinci',
             'təyyarə', 'bərbər', 'elektrik', 'nəsil', 'qara', 'fəsil', 'fikirləşmək', 'milyon', 'oyuncaq', 'süpürgə', 'təməl',
             'yaratmaq', 'çatmaq', 'sınamaq', 'keçirmək', 'kal', 'meyvə', 'fəqət', 'eşq', 'rəsim', 'işıq', 'içmək',
             'xanım', 'xidmət', 'ehtiyac', 'nöqtə', 'qayda', 'cansız', 'oyun', 'artırmaq', 'təkrar', 'tənbəl', 'qısa', 'asan',
             'dəsmal', 'oraq', 'səcdə', 'razılaşmaq', 'rəssam', 'diqqət', 'kompyuter', 'printer', 'gələcək', 'üzüm',
             'isti', 'oğlaq', 'dinləmək', 'uyğun', 'şirvan', 'yeniyetmə', 'metr', 'unutmaq', 'yerimək', 'stol', 'mürgüləmək',
             'çətir', 'ağız', 'duyğu', 'quraşdırmaq', 'hələ', 'şagird', 'birçox', 'izləmək', 'dərəcə', 'mümkün', 'karandaş',
             'divar', 'şəkil', 'sənət', 'menyu', 'xəstəlik', 'qürur', 'televizor', 'bulud', 'masa', 'ölmək', 'komanda', 'üst',
             'kafe', 'musiqi', 'ayılmaq', 'enerji', 'universitet', 'idman', 'güzgü', 'can', 'kilid', 'sayğac', 'ölüm',
             'kofe', 'qaranquş', 'cənnət', 'baha', 'ucuz', 'onlar', 'sabah', 'internet', 'mühəndis', 'mənzərə',
             'mərkəz', 'məchul', 'yerində', 'düzənlik', 'qəsəbə', 'tox', 'aşağı', 'cavab', 'yatmaq', 'səhər', '', 'axşam',
             'sübut', 'götürmək', 'qatılmaq', 'yoxsa', 'paltar', 'ödəmək', 'milliön', 'mesaj', 'xəstə', 'şəhər', 'enmek',
             'cücə', 'stul', 'həftə', 'tıxac', 'hesap', 'avtomobil', 'yad', 'yer', 'mətbəx', 'vərəq', 'lakin',
             'kölgə', 'ayrı', 'qiymət', 'haqqında', 'ağırlıq', 'kassa', 'yalnız', 'hazırlamaq', 'pəncərə', 'sonunda', 'yavaş',
             'lazım', 'dəyər', 'qoca', 'yanlış', 'varlıq', 'artım', 'beton', 'quyu', 'satış', 'içəridə', 'lüks', 'məhtəl',
             'qaya', 'dağ', 'xeyir', 'qorumaq', 'qatil', 'qandal', 'məhkum', 'əl', 'zebra', 'heyvan', 'savaş',
             'mal', 'sac', 'bankrot', 'mala', 'dəyiştirmək', 'dörd', 'düzəltmək', 'səhifə', 'tələbə', 'qurmaq', 'beş',
             'iqtisadiyyat', 'geniş', 'yandırmaq', 'qoxu', 'sağ', 'çimərlik', 'əsr', 'caddə', 'bazar', 'rüzgar', 'quldur', 'sinif',
             'şükür', 'çıxmaq', 'ağır', 'bayraq', 'guşə', 'siqaret', 'daş', 'kəlimə', 'bina', 'eşmək', 'üzmək', 'parti', 'yataq',
             'çəkilmək', 'qorxmaq', 'fəth', 'səbəbkar','sol', 'külək', 'yağ', 'anmaq', 'alışqan', 'vurmaq', 'gülmək', 'darıxmaq',
             'satmaq', 'şir', 'göndermək', 'bacarıq', 'firma', 'hürkütmək', 'ürək', 'hərarət', 'puş', 'şərt', 'surət', 'künc',
             'yaralı', 'model', 'balık', 'məhəllə', 'görüş', 'vətən', 'qonağlıq', 'miqdar', 'birinci', 'meydan', 'ölçü',
             'seçmek', 'zərgər', 'məktəb', 'baxça', 'çörək', 'boy', 'qızdırmaq', 'dolu', 'qurutmaq', 'sənaye', 'uçmaq',
             'yardım', 'qarşılaşmaq', 'market', 'xumarlanmaq', 'yoxlama', 'məşhur', 'balaca', 'gəzmək', 'çiçək', 'işarə',
             'kömək', 'ağcaqanad', 'istək', 'ötən', 'yoxlamaq', 'yoluxmaq', 'addım', 'nərd', 'oğru', 'icazə', 'korku',
             'təhsil', 'polis', 'şər', 'acılamaq', 'fikir', 'tez', 'sap', 'məşğul', 'yosun', 'atəş', 'fərq',
             'yaşma', 'yaşlı', 'sızıldamaq', 'qoşulmaq', 'məhlə', 'mütləq', 'yemək', 'federasiya', 'ləngitmək', 'dayanmaq', 'dar',
             'qaç', 'yaşıllaşdırılma', 'zövq', 'görüntü', 'pəri', 'ders', 'deputat', 'alov', 'canlı', 'silah', 'aso',
             'mükafat', 'xlor', 'fərqləndirmək', 'müzakirə', 'sinema', 'dəyişkən', 'hədəf', 'yuxulamaq', 'dostluq', 'yanmaq',
             'mükafatlandırmaq', 'nanə', 'basmaq', 'kenar', 'kontrol', 'çevirmək', 'din', 'güçlü', 'tor', 'plan', 'beyin',
             'elektrik', 'cahil', 'deşmək', 'ət', 'lampa', 'söyləmək', 'çizgi', 'möhtəşəm', 'alim', 'cild', 'ruh',
             'sevilmək', 'şəlalə', 'nazirlik', 'baxışmaq', 'sahiblənmək', 'irəli', 'ifadə', 'bədən', 'xatırlamaq', 'qüsurlu',
             'yaxmaq', 'dağ', 'bağlamaq', 'addımlamaq', 'ciddi', 'həll', 'say', 'bələdiyyə', 'enli', 'seçim',
             'ağlamaq', 'bağlı', 'serial', 'artırmaq', 'fəaliyət', 'zərər', 'dərin', 'salon', 'çeşidləmək', 'kəsilmək',
             'bağışlamaq', 'sadə', 'qazan', 'sayıqlamaq', 'toplamaq', 'aşkar', 'bağırmaq', 'məsuliyət', 'davranmaq',
             'məktub', 'soymaq', 'canlı', 'iddia', 'makinə', 'yararlanmak', 'yaşlı', 'boş', 'ayaqqabı', 'futbol', 'adminstrator',
             'oğurlamaq', 'müqavilə', 'tutulmaq', 'baxımlı', 'bitki', 'görkəmli', 'dərman', 'borclu', 'yastıq', 'keçərli',
             'mühavizə', 'imkan', 'cəza', 'haqsızlıq', 'dincələmək', 'top', 'psixoloq', 'doldurmaq', 'kanal', 'məkan', 'arı',
             'yıllık', 'dolayısıyla', 'yazılmak', 'ait', 'parmak', 'saymak', 'atılmak', 'belirlemek', 'normal', 'komek',
             'illik', 'qırmızı', 'rol', 'mahnı', 'milyarder', 'hazır', 'bənzəmək', 'qanun', 'dərhal', 'boy', 'günlük', 'mərhələ',
             'günah', 'niyə', 'səhnə', 'soxmaq', 'adət', 'kreslo', 'günahkar', 'sənətçi', 'təhlil', 'uzanmaq', 'təhdid',
             'yollanmaq', 'meşə', 'ayırmaq', 'düzmək', 'faiz', 'genetik', 'əsər', 'hikayə', 'duzlu', 'orman', 'roman',
             'vergi', 'yar', 'aslılıq', 'basın', 'dəstək', 'geyinmək', 'xəta', 'sınır', 'birlik', 'əsarət', 'kəllə',
             'yaralanmaq', 'yetərli', 'sərin', 'qaranlıq', 'valyuta', 'sülh', 'bəbək', 'vətəndaş', 'yerimək', 'küncüd', 'millət',
             'reklam', 'yüksəlmək', 'zirvə', 'aşiq', 'mənbə', 'sosyal', 'qərarlı', 'keçmiş', 'xəstəxana', 'gavalıa',
             'xəyal', 'gazeteci', 'içerisi', 'inanç', 'nitelik', 'üzeri', 'bitirmek', 'gerçekleşmek', 'giriş', 'rahat',
             'topluluq', 'bərabər', 'dükan', 'gizli', 'bənzər', 'dəri', 'oxşamaq', 'mücadilə', 'problem', 'servis', 'fərrari',
             'yaşıl', 'zahiri', 'bahalı', 'təpki', 'cümə', 'arzulamaq', 'azadlıq', 'qəfəs', 'kimlik', 'məsələ', 'üçüncü',
             'cəzalı', 'dəyərləndirmək', 'maraqlı', 'sürücü', 'süd', 'tutqu', 'əşya', 'pələng', 'qoç',
             'ağırlıq', 'milyard', 'tibb', 'sıxıntı', 'tanrı', 'trip', 'küsmək', 'efir', 'qayğı', 'mahal',
             'qram', 'yatırtmaq', 'incə', 'qarışmaq', 'təhlükə', 'hüzur', 'dairə', 'fasilə', 'işləmək', 'mətanət',
             'zəhər', 'kül', 'külqabı', 'vertalyot', 'işarələmək', 'şimal', 'evlənmək', 'burun', 'xeyirli', 'əlbəttə', 'işçi', 'işlətmək',
             'qisas', 'mağaza', 'medya', 'üzərlik', 'bala', 'çıxartmaq', 'sabit', 'sıgorta', 'yaz', 'divan', 'bəndə',
             'sabitləmək', 'hərgün', 'klavyatura', 'risk', 'cəhd', 'sözlər', 'işgəncə', 'duz', 'cəm', 'bağ', 'düşük',
             'etiraf', 'sujet', 'olmaq', 'orqan', 'öldürmək', 'sonra', 'pozmaq', 'pozulmaq', 'hakim', 'leytinant', 'komandir',
             'şirin', 'baca', 'dəyişmək', 'qanunsuz', 'rüzgar', 'kürək', 'yaratmaq', 'zövqlü', 'yeddi', 'azalmaq',
             'yardımlaşmaq', 'menyu', 'əlaqələndirmək', 'müdür', 'otel', 'yaymaq', 'edam', 'avtobus', 'güvənlik', 'hüquq',
             'qılmaq', 'modem', 'vayfay', 'silah', 'naxış', 'ulduz', 'yoğun', 'əsgər', 'bəhs', 'vəfasız', 'qaz',
             'papulyar', 'yetişmək', 'bəyan', 'bəsdi', 'dünən', 'görüşdürmək', 'yeritmək', 'alışveriş', 'bilinçik', 'çərçivə',
             'lazım', 'var', 'tükənmək', 'uzatmaq', 'yönlük', 'at', 'çürütmək', 'məsələlər', 'kart', 'sayt',
             'yaratmaq', 'rəfiqə', 'çiçek', 'halsız', 'sayğı', 'pullu', 'yetki', 'kilo', 'paylaşmaq', 'sərt', 'keratin',
             'çay', 'sülənmək', 'kəsin', 'zəngin', 'heçvaxt', 'sözlü', 'düşmən', 'ticarət', 'aktiv', 'boyamaq', 'cihaz',
             'üzləşmək', 'lambir', 'dostlaşmaq', 'savab', 'qəhrəman', 'kaşki', 'məclis', 'balonka', 'fişəng', 'ünvan', 'ertələmək',
             'saqqal', 'biçarə', 'çarəsiz', 'güvən', 'marka', 'yarpaq', 'yararlı', 'oxatan', 'bərəkət', 'cırmaq', 'düşünülmək',
             'könül', 'xasiyyət', 'irəliləmək', 'şərab', 'yuxarı', 'alt', 'düzəltmək', 'kassir', 'hədis', 'təmiz',
             'vitamin', 'qürurlanmaq', 'təsirlik', 'fəxr', 'yumurta', 'aşxana', 'jurnal', 'yaş', 'kəsdirmək', 'qruz', 'xəbərdarlıq',
             'xəbərdar' 'çarıq' 'şkaf'
             ]


def kelime_sec():
    return random.choice(kelimeler)
