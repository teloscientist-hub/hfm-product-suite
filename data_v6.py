# -*- coding: utf-8 -*-
# v6 content model: the Molly (v2) + Perry (v5) two-way merge, Mario excluded.
# 27 + 32 = 59 source units resolve to 44: 25 Molly primary, 19 Perry primary, 13 Perry folded, 2 Molly dropped.
# Generated 2026-09-12 by gen_v6.py from v2/index.html (S, TY) and data_v5.py (U). Hand-edit freely; counts are recomputed by build_v6.py.
# Source of the dispositions: 00 - The Two-Way Merge, Molly and Perry 2026-09-12.md

TIERS = [{'id': 't0',
  'short': 'Diagnostics',
  'n': 'Tier 0',
  'name': 'Diagnostics',
  'c': 'var(--cyan)',
  'hex': '#3CC2DB',
  'tag': 'One week or less. One finding you did not have. Then decide.',
  'promise': 'Before you spend on AI, find out what is broken, what it costs you, and what the machines '
             'already say about you. Ranked, with the evidence attached.',
  'lede': 'Four short engagements. Three hand you a finding about your own operation with the proof behind '
          'it; the fourth takes an hour and asks the answer engines who you are. Each is small enough to say '
          'yes to and honest enough to tell you something you did not want to hear. After that, the next '
          'decision is obvious.',
  'why': [{'h': 'Improvement money goes to the loudest advocate',
           'p': 'Without a shared diagnosis, budget follows whoever argued best in the last meeting. That is '
                'how a redesigned landing page ends up in front of a broken handover.'},
          {'h': 'A finding travels further than an opinion',
           'p': 'A ranked register with evidence behind each row can be taken into a board meeting. A point '
                "of view cannot. And the model's answer to who you are beats your opinion of your "
                'positioning.'},
          {'h': 'You find out what a week with us is like',
           'p': 'Each of these is a low-risk first engagement. Two of the four end with something fixed or '
                'switched off before we leave.'}],
  'how': 'We measure rather than interview. We walk your journey as a customer would, score your published '
         'work against a fixed rubric, ask your individual contributors what they did last week rather than '
         'asking their managers what the process is, and run the visibility check logged out, because a '
         'signed-in account personalises its own answers. Then we rank what we found with you in the room.'},
 {'id': 't1',
  'short': 'Foundation',
  'n': 'Tier 1',
  'name': 'Foundation and ground truth',
  'c': 'var(--navy)',
  'hex': '#222639',
  'tag': 'What every tool needs to know about you, and what your numbers actually capture',
  'promise': 'Four documents about your company that every tool, assistant and writer reads first, plus the '
             'tracking and the model benchmark that everything above is measured against. Skip this and '
             'everything after it comes out generic, or unmeasured.',
  'lede': 'Six engagements, and two kinds of ground. Four are about the company: voice, customer, '
          'differentiator, positioning, method. Two are about measurement: whether your conversion tracking '
          'captures anything a bot cannot fake, and what each model actually costs you for the quality you '
          'get. This is the tier clients want to skip. It decides whether the rest works.',
  'why': [{'h': 'Your tools are not the problem',
           'p': 'When everything the machine writes sounds like everything else the machine writes, the '
                'cause is almost always that nobody gave it anything category-specific to work from.'},
          {'h': 'Bad signal trains the platform against you',
           'p': 'Bot traffic generating fake conversions is not a reporting problem. The algorithm learns '
                'from it and starts finding more bots. Conversion tracking stopped being measurement and '
                'became defence.'},
          {'h': 'Cost is a routing input, not an afterthought',
           'p': 'The rule is quality over price, but measurable quality over price. The second clause is '
                'what makes it a rule rather than a slogan, and it requires a benchmark.'}],
  'how': 'We build from evidence, not from a workshop. Your voice is extracted from your own best writing, '
         "your customer's language from recorded calls and reviews, your differentiator tested against what "
         'competitors publicly claim. On measurement, events close to the money first, because actions '
         'harder for a bot to fake carry more signal. Then a check that runs at delivery time, because a '
         'standard nobody enforces is a preference.'},
 {'id': 't2',
  'short': 'Revenue',
  'n': 'Tier 2',
  'name': 'Revenue and offers',
  'c': 'var(--red)',
  'hex': '#EE2A52',
  'tag': 'What you sell, how you price it, how you say it, how it moves',
  'promise': 'Line up your offers so each one leads to the next. Price the work to what it recovers. Build '
             'pages that make the case. Plan the launch. And decide, on evidence, whether you are selling a '
             'project, a system or a relationship.',
  'lede': "Nine engagements, and two buyers. Four are about a company's offers: the ladder, the page, the "
          'launch, the pre-sell. Five come out of a practice that installs AI systems for a living and are '
          'about how a services business gets clients, prices, and structures what it sells. Read the second '
          'group only if you run a practice. None of the nine has a model in it that matters, and none '
          'carries a version number.',
  'why': [{'h': 'Offers that share a rung eat each other',
           'p': 'When two products solve a version of the same problem for a version of the same buyer, one '
                "absorbs the other's demand. It does not show up as a loss. It shows up as one product doing "
                'well.'},
          {'h': 'The retainer argument has two sides and we hold both',
           'p': 'One engagement here sells a maintenance retainer, derived from the fact that installed '
                'systems decay. Another argues directly against monthly billing and says to let the client '
                'ask. Which fits depends on whether your buyer experiences your work as a system that '
                'decays, a project that completes, or a relationship that renews. Averaging them would '
                'describe none of the three.'},
          {'h': 'Price to what the client recovers, never to what a naive buyer would pay',
           'p': 'The stated reason is retention. A client who finds out later what the market rate was does '
                'not stay, and it is far cheaper to keep a customer than to find one.'}],
  'how': 'Every offer we specify has to answer what this buyer will still need afterwards, and which of your '
         'products solves that. On pages, we front-load the argument into a structured preparation before a '
         'sentence is drafted. On pricing, three methods and one rule: charge what nobody can undercut, '
         'because a client who feels extracted from is a client you lose.'},
 {'id': 't3',
  'short': 'Content',
  'n': 'Tier 3',
  'name': 'Content and production',
  'c': 'var(--purple)',
  'hex': '#8F5ED8',
  'tag': 'Every piece moves a buyer one belief closer, and reaches them',
  'promise': 'Content built around what a buyer has to believe before they purchase. Creative the platforms '
             'read as genuinely different. Images and video at a measured cost. Email that arrives. And a '
             'program for being named when a buyer asks a machine.',
  'lede': 'Eight engagements, from the beliefs underneath through weekly production, depth, generated images '
          'and video, ad creative, email, and whether answer engines name you. Two rules run through all of '
          'it: every piece exists to install a specific belief about a named offer, and every generated '
          'asset has a model routed to it on quality and cost together, with a date on which that routing '
          'gets reviewed.',
  'why': [{'h': 'A topic calendar is a publishing schedule in a strategy costume',
           'p': 'It answers what shall we post about. It never answers what does this reader have to believe '
                'before they can buy, which is the question that connects content to revenue.'},
          {'h': 'The platform decides what counts as different',
           'p': 'Changing a headline or a background colour is read as the same creative. Six genuinely '
                'distinct concepts is not a style preference, it is the minimum the ranking system will '
                'recognise.'},
          {'h': 'Citation is the new ranking',
           'p': 'Falling traffic is often low-intent traffic now answered in the overview, and it was never '
                'going to convert. Brand mentions across the web, rather than backlinks, are what gets a '
                'business named.'}],
  'how': "We build the belief set in your customer's own first-person language and derive the calendar from "
         'it. Production gets a review gate nothing bypasses, and we are explicit that the engine produces '
         'the base layer of your content and not all of it. On generated assets, the routing table and the '
         'cost per finished asset are deliverables, because a pipeline that cannot show it is cheaper than '
         'what it replaced is a belief, not a pipeline.'},
 {'id': 't4',
  'short': 'Operations',
  'n': 'Tier 4',
  'name': 'Operations',
  'c': 'var(--gold)',
  'hex': '#F1B900',
  'tag': 'Out of your head and onto paper',
  'promise': 'Get how the business runs out of your head and into documents your team can follow. Then give '
             'every number a compared to what.',
  'lede': 'Four engagements on how the company runs: the leadership habits above the systems, the '
          'documentation underneath them, four numbers you can act on, and the revenue leaking out through '
          'failed payments. This is the tier no AI engagement can skip, because you cannot automate what '
          'nobody wrote down.',
  'why': [{'h': 'Growth costs more than it should',
           'p': 'When the operation lives in a small number of heads, every new client and every new hire '
                'adds load to the same people, and the business scales with the least available resource in '
                'it.'},
          {'h': 'You cannot automate what nobody wrote down',
           'p': 'An undocumented operation has a hard ceiling on how much of it can ever be systematised, '
                'whatever tooling gets bought. Tier 6 assumes this tier is done.'},
          {'h': 'Counts without denominators settle nothing',
           'p': 'Revenue up twenty per cent while client count is up thirty is a business getting worse and '
                'reporting a good quarter. Nobody is being dishonest. The number does not carry the '
                'information.'}],
  'how': 'We invert how documentation is normally attempted. Rather than asking somebody to write a process '
         'up, the person who already runs it records themselves doing it and the written process is '
         'generated from the recording. Capture once, reuse many times. On measurement, the hard part is '
         'definition rather than arithmetic, so we settle what counts as a client and a lead in writing '
         'before computing anything.'},
 {'id': 't5',
  'short': 'Working relationship',
  'n': 'Tier 5',
  'name': 'The working relationship',
  'c': '#E0672B',
  'hex': '#E0672B',
  'tag': 'How one person sets up with one model, before any agent exists',
  'promise': 'The setup that makes Tier 6 work: instructions the model actually has, memory that survives '
             'the session, and a protocol for the day the model changes underneath you.',
  'lede': 'Six engagements, and this tier exists because one source shows the same failure over and over '
          'across eighteen months of live sessions. People fail at agent work for reasons that have nothing '
          'to do with agents. No memory file. No guardrails. No preparation. Nothing in the other library '
          'addresses this layer, and filing it under AI systems is how it gets skipped.',
  'why': [{'h': 'Preparation, not prompts',
           'p': 'The single most repeated line in eighteen months of sessions: successful AI automation does '
                'not begin with prompts, it begins with preparation. Skill, research, guardrails, context. '
                'Then prompt.'},
          {'h': 'The model does not read its own changelog',
           'p': 'A new release does not make your existing setup better. Somebody has to ask it to review '
                'what you built with the new capabilities in mind, and almost nobody does.'},
          {'h': 'The ladder became a fork',
           'p': 'Chat, then Cowork, then Code was taught as a progression in January. By July the middle '
                'step had become a destination for a whole class of user. Routing somebody up when they '
                'should go sideways wastes months.'}],
  'how': 'Interview rather than instruct. The strongest single technique in the source is handing the model '
         'a list of questions and having it ask them one at a time until it says it is clear. Every '
         'engagement here is short, and every one is a precondition for something in Tier 6 rather than a '
         'product in its own right.'},
 {'id': 't6',
  'short': 'AI systems',
  'n': 'Tier 6',
  'name': 'AI systems and agent build',
  'c': 'var(--teal)',
  'hex': '#1F7A8C',
  'tag': 'Your people build the brain. Then it remembers. Then it runs.',
  'promise': 'Assistants your own people build. Agents with one named human owner each, one job each, and a '
             'scope fence. A company knowledge base fed from vetted sources that stays current. And the '
             'architecture for running all of it without the bill scaling with the work.',
  'lede': 'Seven engagements that take a company from people pasting the same context into chat windows to '
          'automated work with an org chart, a memory and a maintenance schedule. Three come from a library '
          "about organisational design and four from a practitioner's own running stack, which is why this "
          'tier has both the governance and the plumbing.',
  'why': [{'h': 'Everyone starts every session from nothing',
           'p': 'The first three exchanges of every conversation are the same explanation of who the company '
                'is. It is a small tax paid continuously by everyone, which makes it invisible and large.'},
          {'h': 'One responsibility each, and the fence is the point',
           'p': 'The agent template ends with a clause people skip: you are not doing other work, this is '
                'the only thing you do. Without the fence the specialists drift back into being one '
                'generalist, and without a named human owner nothing improves.'},
          {'h': 'Somebody will ask the governance question',
           'p': 'A board member, a client or a regulator asks what is automated, who is accountable and what '
                'gets reviewed. A company that cannot answer has to stop and find out, usually at the worst '
                'moment.'}],
  'how': 'We train your people to build rather than building for you, because a built assistant is one '
         'assistant and a trained cohort is a capability. Every agent gets one named human owner, never a '
         'team, and no agent publishes without a person in the path. We vet the sources before we build the '
         'brain, build the review gate before we build the agent, model it where iteration is cheap before '
         'we port it, and schedule the maintenance rather than waiting for something to break.'}]

DROPPED = [{'id': 'M11',
  'name': 'Daily Selling Rhythm',
  'from': 'Molly',
  'why': 'Ninety days of support attached to a two-week install. The support tail is the product and HFM '
         'does not staff it.'},
 {'id': 'M24',
  'name': 'Hiring Scorecards',
  'from': 'Molly',
  'why': 'Real, useful, and not a thing HFM sells. It belongs in an operations practice.'}]

U = {}
def u(slug, **k): U[slug] = k


# ---------------- T0 : Diagnostics ----------------
u('client-journey-audit',
 t='t0',
 type='N',
 src='molly',
 src_id='M01',
 name='Client Journey Audit',
 time='1 week',
 who='COO, head of revenue',
 promise='Find where people stop moving through your business. Ranked. One drop-off fixed before we '
            'leave.',
 problem='You spend to bring people in and cannot say where they stop. The top numbers look fine. The '
            'bottom numbers look thin. Every department has its own theory about the middle. Marketing '
            'blames the handoff. Sales blames the leads. Nobody is lying and nobody can prove it.',
 cost='The leak itself is the smaller cost. Every improvement gets aimed at a guess, so budget goes to '
         'whichever stage has the loudest advocate. The stages nobody owns do not get worse loudly. They get '
         'worse slowly. The first signal is a renewal number twelve months later.',
 hard='Journey mapping usually produces a diagram of how the business is supposed to work. Getting the '
         'version that runs means walking it yourself, from every entry point, reading the sequences as a '
         'customer receives them. Then pulling the number at each stage with the denominator stated. The '
         'stages where no number exists are findings on their own. They are also the ones a workshop never '
         'surfaces.',
 work=['We map all four phases live, with everyone who touches the customer in the room. Including the '
          'people who answer the phone',
          'We walk the journey ourselves from every entry point and record what is stale, broken or '
          'contradictory',
          'We pull volume and conversion at each stage from your systems, and mark the stages nobody '
          'measures',
          'We rank the leaks with you on volume and effort. You pick one. We close it with your team '
          'watching',
          'Where paid media is an entry point, we rebuild the ad reporting as columns in the order the '
          'customer moves: reach, click, landing page view, content view, add to cart, checkout, purchase. '
          'Then we read the drop-off between each pair of steps rather than the end number'],
 get=['A one-page journey map where every stage has a named owner',
         'A ranked leak register with the evidence behind each row',
         'Your instrumentation backlog: every stage you currently cannot measure',
         'One leak closed, live, before we leave',
         'A monthly re-audit your own team runs',
         'The funnel-shaped reporting preset, built in your ad account, with the two diagnostic rules '
         'written down'],
 money='Two ways. The leak we close is revenue recovered in the same week. The register stops the next '
          'four quarters of improvement budget landing on the wrong stage.',
 gate='**Two rules we apply to the ad account.** Upstream movement with no purchases means the ad is '
         'alive, not dead. Clicks that never reach the page mean speed or tracking, not creative. Below a '
         'few hundred conversions the pattern is noise, and we say so rather than reading tea leaves.',
 absorbs=['P3 The Funnel-Shaped Reporting Read'])

u('content-scorecard',
 t='t0',
 type='A',
 src='molly',
 src_id='M02',
 name='Content Scorecard',
 time='3 days',
 who='CMO, head of content',
 promise='Two charts that show why good content produces impressions and nothing else.',
 problem='The content is on brand, accurate, and out on schedule. What comes back is impressions and a '
            'few comments from people who already buy from you. The internal conversation has circled for '
            'months: more volume, better distribution, maybe video. Nobody can say what is wrong, because '
            'each piece read on its own looks fine.',
 cost='You keep paying for reach to fix a problem reach cannot fix. Meanwhile the content function loses '
         'its argument for budget. A team that cannot explain what is wrong cannot explain what would be '
         'better, so every request becomes a request for more of the same.',
 hard='Nobody can diagnose content by reading it. Each piece looks fine on its own. The problem shows up '
         'only as a distribution across the whole set, and that needs a fixed rubric two people can apply '
         "and agree on. Building a rubric that explains a company's own best work, rather than one that "
         'scores everything low, is the part that takes experience.',
 work=['We agree a sample of thirty to fifty pieces and calibrate the scoring with you live before '
          'running it',
          'Every piece scored on depth: how much of the persuasive structure it carries, out of seven '
          'elements',
          'Every piece assigned to the stage of buyer awareness it speaks to',
          'Two analysts score independently on an overlap sample, and we publish where they disagreed',
          'We rebuild five of your own pieces, so the difference shows on your material rather than somebody '
          "else's example"],
 get=['A depth distribution chart with the working floor marked',
         'An awareness coverage chart against where your revenue comes from',
         'The full scored dataset, so your team can extend it',
         'Five rewrites showing the original, the score and exactly what changed',
         'The scoring rubric, so new work gets graded before it publishes'],
 money='The coverage chart usually shows a whole stage of buyer awareness the company never speaks to. '
          'That stage is where new demand comes from. Everything else in the tier follows from knowing which '
          'of the two problems costs more.')

u('ai-task-triage',
 t='t0',
 type='A',
 src='molly',
 src_id='M03',
 name='AI Task Triage',
 time='1 week',
 who='COO, CFO',
 promise='A ranked list of what to automate, a cancel list with a dollar figure on it, and one automation '
            'live before we leave.',
 problem='You have an AI budget and no ranked list of where to point it. Someone asked for a strategy and '
            'got a list of tools. Pilots nobody shut down. Licenses renewing on autopilot. One team built '
            'something good that no other team uses. Every proposal in your inbox looks plausible and none '
            'of them can be compared.',
 cost='Money first, and it is usually recoverable in the same week. Nearly every company we look at is '
         'paying for tools nobody has opened in ninety days. The larger cost is build order. Automate '
         'something that still needs a human and you get a system somebody supervises forever. Automate '
         "something nobody wrote down and you get a system that encodes one person's habits, then breaks "
         'when they leave.',
 hard='The census has to come from individual contributors rather than managers. Managers describe the '
         'process as designed. Contributors describe it as run. The triage also has to be willing to take '
         'things off the list. A review that recommends automating everything is not a triage, and holding '
         'that line in a room that has already bought a platform takes some spine.',
 work=['We open by replacing the question in the room. Not what does the tooling cost, but what does each '
          "seat produce, in the holder's own units: drafts, tickets, builds, reels. Cost per seat is uniform "
          'and output per seat is not',
          'We interview eight to fifteen individual contributors about what they repeated last week, not '
          'what they typically do',
          'Every task goes through three questions with your leadership group: does it need a human, can it '
          'be standardized, is it slowing operations down',
          'We compare your software spend against actual usage and against what the backlog needs',
          'We build the top item and leave it running, owned by one of your people'],
 get=['The task census, named by the people who do the work',
         'A ranked backlog with the reasoning behind each rank',
         'A leave-alone list, so nobody re-proposes automating judgment next quarter',
         'The cancellation list with its annual figure',
         'One live automation, and the one-page triage method your managers run next quarter',
         'A per-seat output table, with each before figure marked as measured or reconstructed'],
 money='The cancellation figure is real money off your invoices, and it frequently exceeds the cost of '
          'the engagement. We hold ourselves to that. If it does not, we say so at the readout.',
 gate="**We will not use somebody else's benchmark as your before figure.** Where none exists we "
         'reconstruct one and mark it reconstructed. Trimming an AI budget on cost alone removes the seats '
         'producing the most and keeps the ones producing nothing.',
 absorbs=['P4 The AI Spend-to-Output Audit'])

u('ai-visibility-check',
 t='t0',
 type='A',
 name='The AI Visibility Check',
 time='1 hour',
 who='Founder, whoever owns the brand',
 promise='What the answer engines say when somebody asks who you are, taken live and logged out.',
 problem='You have a positioning statement. Nobody has checked whether the systems that now answer most '
            'questions about your category have ever heard it.',
 cost='A positioning nobody outside the building shares is not a positioning. Businesses spend years '
         'being known for something the market has never associated with them, and the first signal usually '
         'arrives as a lost deal nobody can explain.',
 hard='Almost nothing, technically, and that is the point. What people get wrong is running it signed in. '
         'A personalised account returns answers shaped by your own history, which is how an operator '
         'concludes his clients rank first everywhere when they do not.',
 work=['Two queries, run logged out and in a clean session: who is [your name] and what are they known '
          'for, and the same for the company.',
          'The same queries across more than one engine, because they disagree and the disagreement is '
          'informative.',
          'A competitive pass: the three queries a buyer in your category would actually type, and who gets '
          'named instead of you.',
          'Where the answers came from. The cited sources are the properties actually doing the work, and '
          'they are rarely the ones you have been maintaining.'],
 get=['The verbatim answers, with their sources, across engines',
         'The gap between what you say you are known for and what comes back',
         'The list of properties currently speaking for you',
         'Three queries you are absent from that you should not be'],
 money='An hour, and the cheapest thing on this site. It exists to make the next decision obvious rather '
          'than to become a project.',
 gate='**If the answer comes back empty, that is a finding and not a failure.** Some categories return no '
         'clear leader at all, which makes them cheap to win and changes what we would recommend next.',
 src='perry',
 src_id='P1')


# ---------------- T1 : Foundation and ground truth ----------------
u('foundation-sprint',
 t='t1',
 type='N',
 src='molly',
 src_id='M04',
 name='Foundation Sprint',
 time='2 weeks',
 who='CMO, founder',
 promise='The four documents every AI tool in your company reads first, built from your own material, '
            'with a check that enforces them.',
 problem='Everything the machine writes sounds like what it writes for everyone else. You bought the '
            'tools. People use them. What comes out is competent and unmistakably not you. So it gets '
            'rewritten by hand, which means the tool saved nothing. Or it goes out as is, which is worse.',
 cost='Everything built after this inherits it. Belief-driven content, offer architecture, sales pages, '
         'assistants and agents all read these documents first. Thin input does not produce slightly worse '
         'output. It produces generic output at every stage. Then the tools get blamed. A company concludes '
         'AI does not work for their category, when nothing category-specific was ever supplied.',
 hard='Brand voice work is usually adjectives chosen in a workshop, which is why it changes no output. '
         "Doing it properly means pulling the voice out of a company's own best writing. It means taking "
         'customer language from recorded calls, support threads, intake forms, and reviews of the products '
         'they considered instead of yours. That last source is the one nobody tries. It is where objection '
         'language lives.',
 work=['We collect raw material rather than asking you to summarize it: recordings, support threads, '
          'intake forms, your own best writing',
          'We pull out the patterns: the words your customers use, their frustrations, and what they tried '
          'before you',
          'Voice gets described from your corpus, never chosen from a list of adjectives',
          "Your differentiator gets tested against your competitors' public claims. Anything on both lists "
          'is cut',
          'We build a check that reads every draft against your standard at delivery time, and fails the '
          'ones that do not comply'],
 get=['Brand voice, with every trait citing a real example from your own material',
         'Ideal client, including what they fear and the words they use for their own problem',
         'Differentiator, with what was cut and why',
         'Company details: the factual keystone every tool and assistant reads first',
         'A banned-word standard with a working enforcement check, and a named owner for keeping it current'],
 money='This one makes no money directly. It decides whether the nine engagements after it do. We will '
          'tell you when something you want cannot be delivered well without it, which happens more often '
          'than either of us would like.')

u('positioning-antagonist',
 t='t1',
 type='N',
 src='molly',
 src_id='M05',
 name='Positioning and the Antagonist',
 time='1 week',
 who='CMO, founder',
 promise='Give your positioning something to argue against. Then write down the objection answers your '
            'best salesperson gives in the room.',
 problem='You can say what you do. You cannot say what you are against. Your messaging describes the '
            'product accurately and reads like everyone else in the category, because the category settled '
            'on the same vocabulary years ago. The clearest symptom shows up in objections. When a prospect '
            'raises the real one, your material answers defensively, and a defensive answer confirms the '
            'objection.',
 cost='Your best salesperson handles that objection well in person, with an argument that exists nowhere '
         'in writing. Everyone who does not get that conversation meets the defensive version instead. And '
         'content that argues for something without naming what it argues against has no reason to feel '
         'urgent.',
 hard='The instinct is to name a competitor. That is legally exposed and it ages badly. Worse, it makes '
         'your customer the audience for a fight they do not care about. The real antagonist is a belief, a '
         'habit, or an approach the category still teaches. Finding it means working from what your '
         'customers already tried and what let them down. It also has to be specific enough to draw, and '
         'honest enough to admit why people believed it.',
 work=['We build the positioning narrative in story order rather than as a claims list',
          "We hunt the antagonist in your customers' failed attempts, not in your competitor set",
          'We build one primary antagonist and two to four supporting ones. Each gets an honest account of '
          'why it persuades, not only why it fails',
          'We map each of your five hardest objections to the antagonist that defeats it, and write the '
          'defeat',
          'We load the finished document where your writers and assistants read from, so it gets used rather '
          'than filed',
          'We run the leader queries across your candidate positions and record which fields return no clear '
          'leader at all. Those are cheap to enter. The crowded ones behave like early search, where whoever '
          'is at the top tends to stay'],
 get=['A positioning narrative with the process story written out',
         'A named antagonist set, specific enough that a designer can draw it',
         'The objection map: objection, antagonist, defeat, and where each gets used',
         'A hook and slogan set drawn from the narrative',
         'A placement guide, including where the antagonist sits in a talk',
         'The uncontested fields, named, with what the chosen lane excludes written down'],
 money='The argument your best salesperson makes in the room becomes an asset anyone can use. That is the '
          'first time it has ever been available to the rest of your team.',
 gate='**One lane.** Being credible at several things reads as being the leading name in none of them, '
         "and the systems answering buyers' questions reflect that exactly. If every hat has to stay on, we "
         'would rather say so before starting.',
 absorbs=['P31 Positioning for a Single Lane'])

u('name-your-method',
 t='t1',
 type='N',
 src='molly',
 src_id='M06',
 name='Name Your Method',
 time='1 week',
 who='Founder, product marketing',
 promise='Name the method you already run, so buyers stop comparing you on price.',
 problem='You do something specific and repeatable and it has no name. Your delivery team knows the '
            'sequence. When a prospect asks how you work, the answer gets assembled fresh by whoever is in '
            'the room. You have tried this before. Somebody proposed an acronym, it felt forced, and '
            'everyone stopped using it.',
 cost='You compete on rate. Buyers compare what they can compare, so two firms describing similar '
         'activities get compared on price and availability. Underneath that, an unnamed method has no '
         'reference version. Each senior person runs their own variant, and quality tracks who was assigned '
         'rather than what was promised.',
 hard='The failed attempt is almost always the same mistake: reaching for an acronym before choosing a '
         'shape. An acronym only fits a method whose stages happen to start with cooperative letters. A '
         'framework can take ten shapes. Running your method against several of them before you write '
         'anything is what stops the result feeling forced.',
 work=['We reconstruct the method from three completed engagements rather than from a whiteboard',
          'We keep only the stages that cause a specific, predictable failure when skipped',
          'We test your method against ten possible framework shapes and build rough versions of the best '
          'two',
          'We apply the differentiator test to the framework itself, marking which stages are yours and '
          'which are table stakes',
          'Two live tests. Somebody outside the room plans real work from it. A senior person explains it in '
          'ninety seconds without the diagram'],
 get=['A named framework with every stage specified: inputs, outputs, owner, failure mode, done condition',
         'A production diagram usable in front of a client',
         'The claim split: what is differentiating and what is table stakes',
         'The ninety-second explanation, written, so everyone tells the same story',
         'The authoring guide, so your team names the next method without us'],
 money='A method with a name is something you own and price. An unnamed process is a description of '
          'labor, and labor gets compared on rate. You can come out ahead in that comparison and still be '
          'having the wrong conversation.')

u('differentiator-day',
 t='t1',
 type='N',
 src='molly',
 src_id='M07',
 name='Differentiator Day',
 time='1 day',
 who='Founder, exec team',
 promise='One day to surface the concrete reasons clients choose you, the ones your positioning filtered '
            'out for sounding unprofessional.',
 problem='Your positioning could have been written by any of your competitors. It is true of all of you. '
            'Experienced team. Tailored approach. Meanwhile the real reason clients pick you is something '
            'specific that appears nowhere in your material. Ask a client why they chose you and they say '
            'something concrete you have never written down.',
 cost='The interesting part never reaches the market. It gets filtered out at every draft for seeming '
         'unprofessional. Everything downstream goes generic too, because positioning, offers and content '
         'all read the differentiator as input.',
 hard='The professional register is what removes everything distinctive. A session that starts with '
         'values produces a list of corporate virtues. Getting past that filter takes prompts that lower the '
         'stakes on purpose. It looks absurd for the first half hour, and that is the reason it works. In a '
         'company the differentiator is rarely one person, so the real finding is what repeats independently '
         'across several of them.',
 work=['A facilitated day, four to eight people, business set aside entirely for the first hour',
          'Twenty specifics per person across five prompts, including one deliberately unserious one',
          'We mark what repeats independently across three or more people, and what makes the room lean in',
          "Everything that repeats gets tested three ways. Is it true of how you work. Would a competitor's "
          'list contain it. Does a client ever experience it',
          'Everything gets tagged and kept, because most of what this produces is story material rather than '
          'positioning material'],
 get=['The full captured list, tagged by where it is useful',
         'The repeats, which are firm characteristics rather than personal quirks',
         'Differentiator candidates with their test results shown',
         'Story seeds that feed content and recruiting for a year',
         'The session method, so you can run it with a new team'],
 money='It is the cheapest engagement on the suite and it improves the three around it. It is also the '
          'best qualifier we have. A leadership team that takes this seriously will do the harder foundation '
          'work.')

u('conversion-tracking-install',
 t='t1',
 type='N',
 name='Conversion Tracking Install',
 time='1 week',
 who='Media buyer, developer, whoever owns the site',
 promise='Server-side conversion tracking with events chosen close to the money, and a bot filter that '
            'does not punish real buyers.',
 problem='Browser pixels observe what a browser does, and a bot can do most of it. Fake activity with '
            'realistic names and addresses is now common enough to move the algorithm.',
 cost='This is the failure that compounds against you. The platform learns from whatever you send it, so '
         'bot-generated conversions teach it to find more bots. You do not get a flat result, you get a '
         'worsening one, and the reporting looks fine throughout.',
 hard='Choosing the events. Everything downstream depends on picking actions that are hard to fake and '
         'close to a real transaction, and the temptation is always to instrument the easy ones.',
 work=['Audit what the current pixel is actually firing, and how much of it could be automated.',
          'Select events by proximity to money rather than by convenience, on the stated principle that the '
          'closer an event is to a financial transaction the more valuable its signal.',
          'Build the Conversions API integration server-side, with deduplication against the existing pixel.',
          'Install the honeypot: a hidden form field invisible to humans, with two automation paths '
          'depending on whether it was filled. This replaces CAPTCHA, which modern models answer easily and '
          'which costs you genuine prospects.',
          'Verify with live traffic and compare the two signal sources for a fortnight.'],
 get=['Server-side tracking, live and deduplicated',
         'An event map ordered by proximity to revenue',
         'The honeypot field, installed, with both automation paths built',
         'A fortnight of side-by-side signal comparison'],
 money='One week. There is no AI in this engagement at any point, which is why it is the cheapest thing '
          'here to keep working.',
 gate='**If your site is on a platform that will not accept server-side events, we will say so before '
         'starting** rather than building half of it.',
 src='perry',
 src_id='P5')

u('model-routing-cost-read',
 t='t1',
 type='C',
 name='Model Routing and Cost Read',
 time='1 week',
 who='Whoever holds the AI budget and the technical lead',
 promise='A routing rule for which model does which job, held against a live benchmark rather than '
            'against what was true when you set it up.',
 problem='Work gets sent to whichever model somebody trusts. Usually that is the most expensive one, for '
            'everything, including work that does not need it.',
 cost='Routing by habit is expensive in both directions. You overpay on the bulk of the work and '
         'underperform on the part that actually needed the stronger model, and because the bill is a single '
         'line nobody can see either half.',
 hard='The tiebreaker. The rule that makes this work is quality over price, but measurable quality over '
         'price, and the second clause requires you to have decided what measurement means for each job type '
         'before the routing exists.',
 work=['Classify your recurring AI work by job type: writing, documentation, code, orchestration, '
          'research, image, video.',
          'Set the subscription-first ordering, so the capacity you already pay for is used before anything '
          'is bought by the token.',
          'Build the routing agent, given a live benchmark and instructed to re-read it before each job '
          'class rather than holding a memorised list.',
          'Install the recurring check, because the model list changes weekly and a routing table written '
          'today is wrong within the quarter.',
          'Write the sensitivity rule: which categories of data never leave which vendor. In the source '
          "material this rule lives in the operator's head, and that is the part we fix."],
 get=['A routing table by job type, with the reasoning',
         'The routing agent, reading a live benchmark',
         'A scheduled re-check, with an owner',
         "A written data-sensitivity boundary, in the file rather than in somebody's head"],
 money='One week to build, and it is the engagement on this site most likely to pay for itself inside a '
          'quarter.',
 gate='**This ages faster than anything else we sell.** The scheduled re-check is not an upsell, it is '
         'the reason the engagement is worth buying, and we will not build it without one.',
 src='perry',
 src_id='P6')


# ---------------- T2 : Revenue and offers ----------------
u('offer-ladder-design',
 t='t2',
 type='N',
 src='molly',
 src_id='M08',
 name='Offer Ladder Design',
 time='2 weeks',
 who='Revenue lead, founder',
 promise='A three-rung ladder where every offer names what the buyer needs next and which of your offers '
            'provides it.',
 problem='Your offers compete with each other and your best customers have nowhere to go next. The list '
            'grew by accident. Somebody built a thing for one client, it became a product, and it now sits '
            'beside two others solving a version of the same problem for a version of the same person. Sales '
            'cannot say which one a prospect should buy without a call.',
 cost='Cannibalization you cannot see in the numbers. When two offers occupy the same rung, one absorbs '
         "the other's demand and it reads as one product doing well. Then there is the expansion revenue you "
         'never earn, because a customer who finished and is happy has no designed next step. And every '
         'unnecessary choice you hand a buyer adds time and risk to the deal.',
 hard='The ladder only works if every offer answers two questions offer documents rarely ask. What will '
         'this buyer still need afterwards. Which of your products solves that new problem. Making those '
         'required fields rather than instinct is the whole mechanism. It also means somebody has to decide '
         'what happens to the offers that turn out to share a rung. That decision is political, and it is '
         'why this work stalls without help.',
 work=['Every current offer specified against fifteen fields, using what exists rather than what people '
          'say',
          'We plot your offers on problem size against price, and the overlaps become visible without '
          'anybody arguing for them',
          'Commercial, delivery and finance decide together for each cluster: consolidate, reposition or '
          'retire',
          'We check the distance between rungs. Too close and they cannibalize. Too far apart and buyers '
          'fall out in between',
          'We write the intention and the objective for every offer as separate sentences, which is what '
          'keeps the copy from sounding manipulative'],
 get=['The three-tier ladder, each rung with its promise, price and buyer',
         'Complete fifteen-field specifications including both exit fields',
         'The overlap finding, with a decision recorded against every clustered offer',
         'A transition map: how a buyer moves up, on what trigger, owned by whom',
         'The specification template, so the next offer gets built to the same standard'],
 money='This is the commercial work that moves the most money on the suite. Companies with five products '
          'and no ladder routinely find in one session that three of them share a rung. The expansion path '
          'they never designed turns out to be the cheapest revenue they have.')

u('sales-page-pipeline',
 t='t2',
 type='A',
 src='molly',
 src_id='M09',
 name='Sales Page Pipeline',
 time='1 week per page',
 who='Demand generation',
 promise='One live sales page, and the process that makes the next one take two days instead of six '
            'weeks.',
 problem='A sales page takes six weeks and reads like a feature list. The brief is a product description. '
            'The first draft describes what the thing is. Every department adds the point it cares about in '
            'review. The page ends up complete, accurate, and confirming a decision the buyer already made '
            'somewhere else.',
 cost='When a page takes six weeks, the page becomes the critical path and campaigns get scheduled around '
         'a copy deadline. Without a sequence, quality tracks whoever wrote it and how much time they had. '
         'Your best page and your worst page each represent you to whoever lands on them.',
 hard='Most of the six weeks goes on arguing about what the page should say, and no amount of writing '
         'skill removes that. The fix is a structured preparation finished before a single sentence gets '
         'drafted. Teams find it uncomfortable for about an hour. Holding that line is the difference '
         'between a page and a process.',
 work=['Eleven-step preparation worked through with your team before any copy is written',
          'We structure the same offer five different ways and choose deliberately rather than by habit',
          'Every feature is pushed through to a real benefit, using a mechanic your team can apply in ninety '
          'seconds',
          'Headlines are selected from a generated set rather than written once and defended',
          'Every claim gets traced to evidence or removed. Never softened into a vaguer version of the same '
          'unsupported claim'],
 get=['One live page for a real offer, in your CMS, measured',
         'The completed preparation, plus the blank instrument for every future page',
         'Five structural versions of the same offer as a teaching reference',
         'A claim register showing what is evidenced and what still needs proof',
         'A written production sequence with roles, gates and expected durations'],
 money='Page two takes two days. Across a year of campaigns that is the difference between marketing '
          'setting the schedule and the copy deadline setting it.')

u('launch-design',
 t='t2',
 type='N',
 src='molly',
 src_id='M10',
 name='Launch Design',
 time='2 weeks',
 who='Revenue lead',
 promise='An eleven-stage launch you can run again, with the dead middle planned and the people who did '
            'not buy sorted by why.',
 problem='Launches spike once and die. Sales come in on day one, then almost nothing, then a small bump '
            'at the deadline that everyone credits to urgency. The middle is dead because nobody planned the '
            'middle. Or there is no launch at all, and revenue arrives whenever sales makes it arrive.',
 cost='The dead middle is the largest single loss. In a launch of any length, the middle is where most of '
         'your audience is still deciding. Then everyone who did not buy gets treated as one group and '
         'receives the same follow-up, or none. They did not buy for opposite reasons.',
 hard='Launch sales follow a predictable double-peaked shape. Knowing the shape is not the same as using '
         'it. The second peak has to be built with something that did not exist at open, which means it goes '
         'into the calendar before the launch starts. A spike planned during the dip arrives after it.',
 work=['We map all eleven stages and fill your version of each, with an owner and a date',
          'The trigger event gets chosen on evidence rather than defaulting to a webinar',
          'Three sequences specified message by message, with the follow-up built at nine steps rather than '
          'three',
          'The mid-launch event is placed in the calendar with an owner before the launch opens',
          'We build reason capture and two opposite routes into your CRM, so non-buyers are split rather '
          'than blanketed'],
 get=['The eleven-stage launch map, owned and dated',
         'A trigger event decision with the reasoning recorded',
         'Show-up, cart-open and follow-up sequences, specified',
         'Live post-close segmentation in your CRM, tested both ways',
         'A belief-assigned run-up calendar and a run-book so the next launch is not built from scratch'],
 money='Post-close segmentation is where the recoverable revenue sits, and it is the part that rarely '
          'gets built. People who did not buy because of money need something smaller. People who did not '
          'buy because they wanted more support need more, since that is a buying signal rather than a '
          'request for a discount. Half your non-buyers have been getting the wrong message.')

u('pre-sell-sprint',
 t='t2',
 type='N',
 src='molly',
 src_id='M12',
 name='Pre-Sell Sprint',
 time='5 days',
 who='Founder, product',
 promise='Find out whether anyone will pay for the thing before you build it. Five days. Payment is the '
            'only signal we count.',
 problem='You have a twelve-month roadmap and no way to know whether anyone wants what is on it. Every '
            'item is a bet and every bet resolves the same way: build it, ship it, find out. By then the '
            'budget is spent, and admitting it did not work costs more than calling it phase one.',
 cost='You learn what customers want at the most expensive possible moment. After the build, when sunk '
         'cost makes the answer hard to hear. And speed becomes a capability you do not have, so '
         'opportunities in a moving category go to somebody else as a matter of structure rather than luck.',
 hard="Pre-selling works, and it assumes nobody else's job breaks when you do it. In a company that is "
         'untrue. The adaptation is one meeting: finance, legal and support agree the price, the delivery '
         'date and the refund position before anything is published. The other hard part is setting the go '
         'or no-go threshold before you see the data. Renegotiating it afterwards is the most likely failure '
         'and the most damaging.',
 work=['Three independent research passes on the subject, merged, treating what all three surface as the '
          'finding',
          'Offer candidates generated by asking what your customers could be helped to do rather than what '
          'you could do',
          'A pre-commitment review with finance, legal and support before anything is published',
          'A validation offer published, with every response worked by hand and recorded',
          'Build in two days if the threshold is met. Stop and write the finding if it is not'],
 get=['The merged research, showing where the three passes disagreed',
         'Offer candidates with the selection reasoning recorded',
         'The pre-commitment record and the refund position',
         'A named lead list, with what each person said they wanted',
         'A live offer, or an evidenced decision not to build one, plus the method so your team runs the '
         'next sprint'],
 money='Interest expressed in a research call and interest expressed with a payment are different '
          'signals, and only one predicts revenue. A sprint that ends in a decision not to build is a '
          'successful sprint. It costs five days instead of two quarters.')

u('pricing-architecture',
 t='t2',
 type='N',
 name='Pricing Architecture',
 time='1 week',
 who='Founder, whoever writes the proposals',
 promise='Three pricing methods, matched to the three situations they each work in, with an explicit rule '
            'against extraction.',
 problem='Pricing is set by instinct and defended by anecdote. The same service goes out at wildly '
            'different numbers depending on how the conversation went.',
 cost='Underpricing is the obvious loss. Overpricing a buyer who does not know the market is the '
         'expensive one: they find out, they leave, and they tell people. The source is blunt that a client '
         'who discovers they were taken will resent it permanently.',
 hard='Knowing which method applies. Markup works for tooling-based services, value-based works where the '
         "client's recovery is measurable, time-based is the fallback for low volume. Applying the wrong one "
         'produces a number you cannot defend in the room.',
 work=['Establish hard cost per service, including tooling and delivery time.',
          'Apply the markup method where the service is tooling-based: ten to twenty times hard cost plus '
          'implementation.',
          'Apply value-based pricing where recovery is measurable: count the missed calls, the lost leads, '
          'the unbilled hours, and price against the recovered amount.',
          'Use time-based as the fallback for clients with too little volume for either.',
          'Install the anti-extraction rule: price where nobody can undercut you, because retaining a client '
          'costs less than acquiring one.'],
 get=['A rate structure with three methods and the trigger for each',
         'Hard cost per service, calculated',
         'A value-based worksheet for the measurable cases',
         'The anti-extraction rule, written into the process'],
 money='One week. No AI in it anywhere, and it will not need revisiting when the models change.',
 gate='**We will argue against your highest defensible price.** The rule here is deliberately not '
         'revenue-maximising in the short term, and if that is not what you want, this is the wrong '
         'engagement.',
 src='perry',
 src_id='P28')

u('one-off-first',
 t='t2',
 type='N',
 name='The One-Off-First Sequence',
 time='1 week',
 who='Founder, sales lead',
 promise='A sales sequence that opens with a single transaction and lets the recurring relationship be '
            'asked for rather than proposed.',
 problem='Every piece of advice in the market says to sell recurring revenue first. Buyers are '
            'increasingly tired of being billed monthly, and the ask is large at the exact moment trust is '
            'smallest.',
 cost='Leading with a retainer maximises the size of the first decision. Most prospects decline it and '
         'would have said yes to something smaller, so the pipeline reads as poor fit when it is actually '
         'poor sequencing.',
 hard='Holding the line when the one-off closes well. The instinct is to convert immediately. The '
         'sequence works because the client asks, and asking too early resets it.',
 work=['Design the one-off: small, complete, genuinely useful on its own, and not a trojan horse.',
          'Price it to be an easy yes and deliver it visibly better than expected.',
          "Do not propose the ongoing. Let the second conversation start from the client's side.",
          'Build the ownership variant for buyers who want to own an agent for a flat fee rather than '
          'subscribe to one.',
          'Track which clients ask, and how long it takes, so the sequence is measured rather than '
          'believed.'],
 get=['A one-off offer, specified and priced',
         'A delivery standard for it',
         'The ownership-model variant',
         'A tracking measure on ask rate and time to ask'],
 money='One week to design. It changes the shape of the pipeline rather than the volume.',
 gate='**This contradicts the maintenance retainer above and we are not going to hide that.** Both come '
         'from the same practice, four days apart. Which one fits depends on whether your buyer experiences '
         'your work as a system that decays or as a project that completes.',
 src='perry',
 src_id='P29')

u('ownership-offer',
 t='t2',
 type='N',
 name='The Ownership Offer',
 time='2 weeks',
 who='Founder designing what to sell next',
 promise='An offer built around the client owning the system rather than renting it, and the service '
            'business that sits on top.',
 problem='Everything is sold as a subscription because the industry decided that was the model. Buyer '
            'preference has moved and most offers have not.',
 cost='Selling only a subscription loses every buyer who wants to own the thing, and that is now a '
         'significant share. It also caps you at the software margin when the durable revenue is in being '
         'the person who runs it.',
 hard='Separating what should be owned from what should be ongoing. The system can be owned; the '
         'maintenance cannot be, because the decay is continuous. Getting that line wrong produces either an '
         'unsustainable promise or an offer nobody wants.',
 work=['Define the ownable unit: what the client buys once and holds.',
          "Price it against the flat-fee alternative rather than against a subscription's lifetime value.",
          'Define the service layer that sits on top, which is where the durable revenue is.',
          'Build the hundred-small-clients version of the model as the alternative to a few large ones.',
          'Write the handover so ownership means something rather than being a licence in different words.'],
 get=['An ownable unit, defined and priced',
         'A service layer on top of it',
         'A handover standard that makes ownership real',
         'A model comparison against your current structure'],
 money='Two weeks. It is an offer design engagement, not an implementation.',
 gate='**This rests on a prediction rather than a measurement.** The claim that buyers are moving back to '
         "ownership is one practitioner's reading of his own market, and we will present it as that rather "
         'than as a trend.',
 src='perry',
 src_id='P32')

u('results-in-advance',
 t='t2',
 type='N',
 name='Results-in-Advance Outreach',
 time='2 weeks',
 who='Founder, whoever does business development',
 promise='An outreach sequence that leads with work already done rather than with a request for a '
            'meeting.',
 problem='Cold outreach asks for time before it has given anything. Response rates reflect that, and the '
            'response is usually to send more of it.',
 cost="Volume outreach with nothing in advance burns the list and the sender's name at once. You get a "
         'low response rate and a reputation, and both are hard to reverse.',
 hard='Doing the work before the yes. Every part of this is easy except the part where you produce '
         'something real for somebody who has not agreed to anything, which is precisely why so few do it.',
 work=['Identify a narrow target set where the same improvement is visible from outside.',
          'Do the work first: the rebuild, the audit, the fix, actually produced.',
          'Send something physical that gets opened, with the work attached.',
          'Let them name the price on the first transaction, so the first exchange is not a negotiation.',
          'Offer the obvious adjacent service at the point of delivery, since the relationship is now '
          'established.'],
 get=['A target set and the repeatable improvement for it',
         'A physical send that gets opened',
         'A first-transaction structure with the price left open',
         'A measured response rate on your own sends'],
 money='Two weeks to build the sequence. The per-send cost is real and is the reason the targeting has to '
          'be narrow.',
 gate="**The outcome numbers in the source are one practitioner's self-report on an unstated sample.** "
         'Seventy-five per cent response and a seven-hundred-and-fifty average are what he said, not what we '
         'measured, and we will not quote them to you as evidence.',
 src='perry',
 src_id='P30')

u('maintenance-retainer',
 t='t2',
 type='A',
 name='The Maintenance Retainer',
 time='Ongoing',
 who='You, if you sell AI systems. Your client, if you buy them',
 promise='A recurring service built on the fact that AI systems decay, priced against an observed '
            'property rather than a pricing tactic.',
 problem='AI systems are sold as builds. Models change, APIs change, vendor instructions change, skills '
            'go stale, and six months later the thing works worse than it did at handover.',
 cost='For the buyer, a system that quietly degrades is worse than one that fails, because nobody '
         'investigates. For the seller, a one-time build means the relationship ends exactly when the decay '
         "starts and the client's experience of your work is its worst version.",
 hard='Nothing to build. The difficulty is that this is usually invented as a pricing strategy and '
         'therefore sold unconvincingly. Derived from the decay instead, it is a genuine need and sounds '
         'like one.',
 work=['Monitor vendor documentation and change logs on a schedule.',
          'Update agents, skills and vendor files when the model underneath changes, in the correct order.',
          'Test performance against real tasks rather than self-reports.',
          'Resolve compatibility issues as vendors move.',
          'Report what changed and what it cost, so the retainer is auditable rather than assumed.'],
 get=['Scheduled monitoring, with an owner',
         'Updates applied in the correct order',
         'Real-task performance testing',
         'A change report each period'],
 money='Ongoing. **The most directly transferable commercial idea in the source material**, and the only '
          'one derived from an observed property rather than asserted.',
 gate='**Read this against the engagement below it, which argues the opposite.** The same practice sells '
         'this retainer and argues against monthly billing four days apart. We hold both positions and will '
         'tell you which fits your buyer rather than pretending there is one answer.',
 src='perry',
 src_id='P27')


# ---------------- T3 : Content and production ----------------
u('buying-beliefs-map',
 t='t3',
 type='N',
 src='molly',
 src_id='M13',
 name='Buying Beliefs Map',
 time='1 week',
 who='CMO',
 promise='Replace the topic calendar with the beliefs a buyer has to hold before they purchase.',
 problem='Your content calendar is organized by topic. Somebody lists themes, somebody assigns them to '
            'weeks, and the output answers what should we post without ever answering what does this reader '
            'need to believe. The content is informative and inert. When a piece performs, nobody can say '
            'why, so it cannot be repeated.',
 cost="Content and revenue never connect, which is why the content team's contribution gets argued about "
         'every budget cycle and never settled. And nothing accumulates. Twelve months of publishing leaves '
         'you with an archive rather than a case.',
 hard='The seven belief categories look like a checklist. They are a sequence. Four of them form a '
         'ladder, running from readers who do not know they have a problem through to readers deciding '
         "between you and a competitor. Beliefs also have to be written in the customer's own first person. "
         'The category everyone gets wrong on the first pass is the one that must not mention your offer at '
         'all.',
 work=["We build the belief set for one named offer, in the customer's first-person language, using their "
          'recorded words',
          'Seven categories, three to five beliefs each, with the ladder structure mapped onto four stages '
          'of buyer awareness',
          'We plot your existing content against the same map, which usually reveals a stage you never speak '
          'to',
          'Objection beliefs written from what sales hears, and urgency written only where it is real',
          'One belief assigned to each week of the next quarter, sequenced by awareness stage'],
 get=["The belief table, first person, in your customer's language",
         'The awareness map, with the ladder shown',
         'A coverage finding naming the stage your content never addresses',
         'A derived quarterly calendar with a brief per week',
         'The method, so the next offer gets its own belief set without us'],
 money='This is the decision that turns a posting schedule into a sales system. Every piece afterwards '
          'exists to install a specific belief about a named offer, which is what connects content spend to '
          'revenue.')

u('weekly-content-system',
 t='t3',
 type='A',
 src='molly',
 src_id='M14',
 name='Weekly Content System',
 time='3 weeks',
 who='Head of content',
 promise='A weekly production system your own team runs, fed by a bank of your real stories.',
 problem='Content production eats a team and produces a trickle. Three people are busy. Output is four or '
            'five pieces in a good week, and good weeks are the ones without a launch or a conference. You '
            'tried AI tools. They produced volume that needed so much editing the editing became the '
            'bottleneck.',
 cost='Consistency is the thing you never get, and consistency is what compounds. Sporadic publishing '
         'never builds an audience, so every piece starts cold. And your most expensive people spend their '
         'week deciding what to post rather than deciding what to argue.',
 hard='The honest constraint is that a content engine produces the base layer, not the whole function. It '
         "cannot write your human material and it cannot supply your opinion on this week's news. Companies "
         'sold an engine as the complete answer end up disappointed by a system working correctly, so we say '
         'this at kickoff and again at handover. The other hard part is the story bank. The material sits in '
         "people's heads and decays in about a month.",
 work=['We measure your current state rather than describing it: pieces, hours, elapsed time from brief '
          'to publish',
          'We design your week rather than importing a template, with each slot given a stated job and '
          'awareness stage',
          "We seed the story bank from your people's specific results, origins and failures, then install a "
          'capture routine inside a meeting that already exists',
          'We build the pipeline end to end with a review gate nothing bypasses',
          'In week three your team runs it for a full week while we sit alongside and fix what breaks'],
 get=['A weekly shape derived for your audience, with the reasoning recorded',
         'A quarter planned and briefed from your belief calendar',
         'A seeded story bank and a one-question weekly capture routine with a named owner',
         'The production pipeline running in your own tooling',
         'An operating document written from the week your team ran it, and a plain statement of what the '
         'engine does not cover'],
 money='Throughput goes up and senior hours per piece go down, both measured against a baseline we take '
          'in week one. The story bank is the sleeper. It is the single biggest factor in whether AI search '
          'results cite you.')

u('copy-depth-workshop',
 t='t3',
 type='N',
 src='molly',
 src_id='M15',
 name='Copy Depth Workshop',
 time='3 days',
 who='Content team',
 promise='Teach your writers to layer, then republish twenty existing pieces in the same three days.',
 problem='The content is correct, complete, and easy to scroll past. Every piece answers its question, '
            'gets skimmed, and gets forgotten, because it opens with the answer and gives the reader no '
            'reason to stay. Your writers are doing what corporate writing taught them: lead with the '
            "conclusion and do not waste anyone's time.",
 cost='Distribution has to work harder than it should. A paid problem created by an unpaid one. And your '
         'existing library is dormant capital: hundreds of pieces that were expensive to produce and are '
         'doing nothing.',
 hard='The change that produces the most result is the one that produces the most resistance: moving the '
         'answer to the end. That is correct advice for a memo to somebody who has to act. It is wrong for a '
         'feed where the reader has not yet decided to care. The argument has to be had in the room rather '
         'than deferred. A team that was told applies it badly. A team that argued it applies it properly.',
 work=['We teach the seven persuasive elements on your own published work, counting layers rather than '
          'passing judgment',
          'We rebuild one of your pieces live, then run the argument about moving the answer to the end',
          'Three alternative structures, with a rule for choosing between them based on how aware the reader '
          'is',
          'Your writers rework and republish twenty existing pieces with us alongside, in a single '
          'supervised day',
          'We write a minimum standard into your process, with a check that is a count rather than a '
          'judgment'],
 get=['The seven-layer checklist, usable in under two minutes per piece',
         'Three remix structures with the selection rule',
         'Twenty republished pieces, reworked by your own writers',
         'A three-layer floor written into your content standard, with an enforceable check',
         'A measurement baseline so the effect can be read in a month'],
 money='It is the fastest content result available, because it works on material that already exists. '
          'Take a published piece, find its single layer, add one ingredient, republish. That is a same-week '
          'result.')

u('ai-image-system',
 t='t3',
 type='C',
 src='molly',
 src_id='M16',
 name='AI Image System',
 time='1 week',
 who='Brand, design',
 promise='A visual identity specific enough that anyone on your team can generate on-brand images, so '
            'design stops being a waiting line.',
 problem='Every image looks like it came from a different company. Your brand guidelines cover the logo, '
            'palette and typefaces, and say nothing about what a generated image should look like, because '
            'they were written before anyone could generate one. Each person making an image makes a '
            'different call. The design team becomes a waiting line.',
 cost='When only the design team can produce something on brand, every piece of content waits for them. '
         'That wait sets the pace of the whole function. And visual recognition never accumulates, so every '
         'impression starts from zero.',
 hard='Naming a visual identity in terms a tool can act on is harder than it sounds. The first three '
         'attempts are always adjectives that could describe any company. The test is generative. The '
         'identity that produces recognizably distinctive output is the right one. There is also a palette '
         "check that rarely gets run, and it regularly shows that some brand colors make the company's own "
         'people look washed out.',
 work=['We name the identity as an era, a feeling and an aesthetic, then test candidates by generating '
          'against them',
          'We test your palette against real photographs of your real people, and produce a rule about which '
          'colors stay away from faces',
          'A prompt library organized by the formats you make, built for selection rather than composition',
          'A one-page table of fixes for the failures that waste the most time: drifting faces, plastic '
          'skin, unwanted text',
          'Your team generates real images for real upcoming content with us alongside',
          'Model choice routed by asset type on quality and cost together, with a review date, because a '
          'routing choice made today is wrong within a quarter'],
 get=['A named visual identity with the test outputs that justified it',
         'Palette rules including the face rule, and aspect ratios by destination',
         'A prompt formula and a selectable library',
         'The fix table, on one page',
         'A style guide, and a boundary agreed with your design lead about what still comes to them',
         'A routing table by asset type, with the date it gets reviewed'],
 money='It removes the routine queue in front of your design team, which is usually the constraint on how '
          'fast the whole content function can move.',
 gate='**Every image model named in this engagement will be wrong within a year.** The review cadence is '
         'part of the engagement, not an upsell, and we will not build the library without it.',
 absorbs=['P22 AI Video and Image Pipeline, image half'])

u('ai-video-voice-system',
 t='t3',
 type='C',
 src='molly',
 src_id='M17',
 name='AI Video and Voice System',
 time='2 weeks',
 who='Content, communications',
 promise='Bring the cost of a video down far enough to publish weekly, and stop generated video from '
            'looking fake.',
 problem='Video costs too much per piece to do weekly. Every one is a small production, so video gets '
            'saved for launches and events, which means the format that holds attention best is the one you '
            'use least. The team tried generative video and found tools that impress in a demo and look '
            'slightly wrong in production.',
 cost='Your best explanations stay unrecorded. The person who explains the thing well does it live, on '
         'calls, over and over. And the formats with the cheapest attention are exactly the ones a '
         'production-scale process cannot feed.',
 hard='Two things. A video with no route into a conversation has done half a job. That is a structural '
         'failure rather than a production one, and it has nothing to do with quality. Second, generated '
         'video reads as fake for a specific and fixable reason. Teams that skip the three-minute fix '
         'produce the uncanny output that gets a whole program vetoed.',
 work=['We start with strategy: which formats you will sustain and what belief each installs. One '
          'required field: what conversation each starts, and who picks it up',
          'Three distinct voice clones per presenter rather than one, recorded as three different sessions',
          'Transcript-based editing installed and trained, which turns editing from a specialist skill into '
          'a writing skill',
          'A required pre-animation routine that removes the waxy quality, taught as a fixed step rather '
          'than a tip',
          'An explicit written decision on avatars, with our recommendation and its reasoning',
          'Model choice routed by task, and cost per finished asset measured against what it replaced, so '
          'the pipeline can show it is cheaper rather than believe it'],
 get=['Three voice clones per presenter with usage notes',
         'Transcript-based editing running, with one real video edited',
         'The video prompt formula in your library, plus the de-waxing routine',
         'A format and route map where no format lacks a next step and an owner',
         'A written avatar decision, so the question stays settled',
         'A routing table with cost per finished asset, measured against the prior method'],
 money='Cost per video falls against a baseline we take in week one. We will also tell you plainly where '
          'we do not recommend a presenter avatar, and give you the reasoning. The recommendation and the '
          'capability stay separate on purpose.',
 gate='**Every video model named in this engagement will be wrong within a year.** The review cadence is '
         'part of the engagement, not an upsell. The one cost figure behind this in the source is a single '
         'self-reported case, and we take our own baseline in week one rather than repeating it.',
 absorbs=['P22 AI Video and Image Pipeline, video half'])

u('newsletter-system',
 t='t3',
 type='N',
 src='molly',
 src_id='M18',
 name='Newsletter System',
 time='1 week',
 who='Lifecycle marketing',
 promise='Get the newsletter running with a named owner, and a one-page email standard your team will '
            'follow.',
 problem='The list gets mailed when somebody remembers. It was expensive to build. It is the only '
            'audience you own outright. It gets a promotional email during a campaign and nothing in '
            'between. There was a newsletter once. It ran five months and stopped the way these things stop: '
            'one skipped week that never restarted.',
 cost='You are renting attention while you already own some. A list that hears from you only when you '
         'want something stops opening, and reactivating it later costs more than maintaining it would have. '
         'Meanwhile campaign emails underperform for structural reasons that are entirely fixable.',
 hard='Newsletters die from depending on somebody having a clear afternoon. Ideas are never the shortage. '
         'The routine has to be designed around that constraint, and the row nobody ever writes down is what '
         'happens in a week when it cannot be written. That single missing rule turns one skipped week into '
         'a canceled newsletter.',
 work=['If the sending domain is new, or the list has gone cold, we warm it before the first issue: '
          'dedicated sending subdomains, five hundred on day one, five hundred on day two, gradual increases '
          'as reputation establishes',
          'Where SMS is in the plan, the messaging registration is prepared before it is submitted: separate '
          'promotional and service consent boxes, live Terms and Privacy pages linked inside the forms, no '
          'conflicting chat widget on a form page',
          'We subscribe to your own list and record what a new subscriber receives, which routinely surfaces '
          'sequences naming products you retired',
          'We build a six-rule standard with your writers on your own recent emails, not on examples',
          'We design the production routine around the constraint that killed the last one, including the '
          'missed-week rule',
          'The first issue is written with your owner rather than for them',
          'We fix the stale sequences we found and rewrite your last campaign against the standard'],
 get=['The newsletter live, with a template, measurement and a named owner',
         'A production routine: owner, fixed slot, inputs, length, missed-week behavior',
         'A quarter of issues planned from your belief calendar',
         'A one-page email standard attached to your review check',
         'The sequence audit, with the stale items fixed',
         'Dedicated subdomains and a warm-up schedule, where the domain needed one'],
 money='It is the only channel a platform cannot take away from you. And the structural fixes are free: '
          'one call to action outperforms three, and subject lines written for curiosity outperform ones '
          'written for clarity.',
 gate='**Deliverability is upstream of everything here.** A newsletter sent at volume from a cold domain '
         'is judged on results it never had a chance to produce. We will not shorten the warm-up because a '
         'launch date moved. No AI at any point in this engagement.',
 absorbs=['P26 Email Infrastructure and Warm-Up'])

u('aeo-authority-program',
 t='t3',
 type='C',
 src='molly',
 src_id='M19',
 name='AEO and Authority Program',
 time='2 weeks, then monthly',
 who='CMO, SEO owner',
 promise='Find out whether ChatGPT, Claude and Google name you when a buyer asks. Then run a monthly '
            'program, measured against the same questions, to change the answer.',
 problem='Your buyers now ask an AI assistant what the options are in your category, and something '
            'answers. You do not know whether it names you. You do not know who it names instead. Your SEO '
            'reports do not cover this. Nobody has checked because nobody knows what checking looks like.',
 cost='You cannot manage what has never been measured, and the absence of a number is the real problem. '
         'Every other channel has one, so this one gets no budget until it becomes a visible loss. Category '
         'answers also settle and then persist, which makes arriving late more expensive than arriving '
         'early.',
 hard='Nobody controls what a model says, and any agency claiming otherwise is selling something. What '
         'you can control is what exists to be cited, and how it is structured. The discipline is a fixed '
         'query set that does not drift. A set that changes after a bad month cannot be compared. The other '
         'discipline is honest reporting in the months when nothing moved.',
 work=['Before the query set, an authority inventory: the proof you already hold, results, worked cases, '
          'stories, lessons, and where each is currently published, which is usually nowhere. Authority does '
          'not require a title',
          'We build a fixed set of fifteen questions with you across brand, category and the problems buyers '
          'describe before they know you exist',
          'We record verbatim what each major assistant currently returns, including who is named instead of '
          'you',
          'A long-form structure built on the specific evidence and stories inside your business, rather '
          'than category explanation anyone could write',
          'The publishing routine attaches to your existing content pipeline rather than adding a separate '
          'workload',
          'Every month we re-run the same fifteen queries and report before and after, per query',
          'Three content anchors for the year, as themes rather than ideas, so the publishing routine has a '
          'spine',
          'Where organic traffic has fallen, we read the Search Console tell before anything else: rankings '
          'stable, impressions up, clicks falling is citation displacement, not a technical fault. Then we '
          'separate the traffic that left from the traffic that converted, because informational queries now '
          'answered in the overview were never going to convert, and we shift the measure to brand mentions '
          'across the web rather than backlink counts',
          'We request indexing in Search Console for every page that carries one of your answers, so the '
          'baseline is taken against pages the engines have actually read, and we confirm the '
          'two-to-three-day recrawl afterwards'],
 get=['The query set and a dated verbatim baseline',
         'The competitor picture: who gets named instead of you, and in what terms',
         'A long-form structure with two pieces built to it',
         'The audit method, runnable by your team without us',
         'Monthly reports with what moved, what did not, and what to publish next',
         "The proof inventory with each item's current visibility, and three content anchors for twelve "
         'months',
         'A diagnosis of what your traffic drop actually was, where there was one, with the Search Console '
         'tell shown rather than asserted',
         'The conversation for the morning the traffic report looks bad, scripted in four lines: the drop is '
         'industry-wide and not our failure, the traffic lost was mostly people who were never going to buy, '
         'we are moving from chasing rankings to earning citations, and here is the new scorecard'],
 money='The measurement is the part that rarely gets built, and it is what makes the program defensible. '
          'You will know your position monthly, which is more than your competitors have.',
 gate='**We will not promise a citation position.** These systems are nondeterministic. The same query '
         'returns materially different answers hours apart, so the monthly is sold as measurement and '
         'compliance, never as a placement. The baseline is taken logged out, because a signed-in account '
         'personalises its own answers and will tell you what you want to hear. The scorecard that replaces '
         'sessions and rankings has three lines: branded versus non-branded split, citation footprint, and '
         'branded search volume trend.',
 absorbs=['P2 Digital Presence and Authority Audit',
             'P24 The Organic Visibility Program',
             'P25 Answer Engine Positioning'])

u('creative-concept-set',
 t='t3',
 type='A',
 name='The Creative Concept Set',
 time='2 weeks',
 who='Head of growth, creative lead',
 promise='Six genuinely distinct creative concepts, built so the platform reads them as different rather '
            'than as variants.',
 problem='Testing produces variations: a new headline, a different background, another cut. The account '
            'fills up and the learning rate does not move.',
 cost='The platform recognises a swapped headline or a recoloured background as the same creative, so a '
         'test budget spread across variants buys you one result at the price of twenty. The account looks '
         'busy and learns nothing.',
 hard='Separating a message from its dressing, which a team inside the account cannot reliably do about '
         'its own work. The distinction has to come from outside or it does not come.',
 work=['Audit what is actually in the account: how many distinct messages sit behind the asset count.',
          'Build against the six concepts as six different conversations rather than six formats: '
          'problem-unaware, harsh truth, testimonial, founder story, comparison, benefit-driven.',
          'Map each concept to a stage of customer awareness, so the set covers the journey rather than '
          'clustering.',
          'Produce a first wave, one per concept, and measure the spread rather than the winner.',
          'Hand over the classification method, since this has to run continuously.'],
 get=['A message count for your existing account',
         'Six concepts, mapped to awareness stages',
         'A first production wave, one per concept',
         'The classification method, transferred'],
 money='Two weeks. It assumes an account with enough spend for a spread to mean something.',
 gate='**This is not a creative production retainer.** We build the set and the method; producing at '
         "volume against it is work for the image and video systems in this tier or your own team's.",
 src='perry',
 src_id='P21')


# ---------------- T4 : Operations ----------------
u('operations-install',
 t='t4',
 type='N',
 src='molly',
 src_id='M20',
 name='Operations Install',
 time='3 weeks',
 who='COO',
 promise='Build how the business runs in the order that sticks: leadership habits first, then the client '
            'journey, then the backend systems.',
 problem='The business runs out of a few heads and one of them is yours. Things work because specific '
            'people know what to do, and the knowing was never written down. You can feel the ceiling. Every '
            'new client and every new hire adds load to the same people. The answer has been to work harder, '
            'because building something needs a clear week that never comes.',
 cost='Growth costs more than it should. Quality tracks who was assigned rather than what was promised. '
         'And you cannot delegate what has never been described, which is why hiring has not relieved the '
         'pressure.',
 hard='Everyone wants to start at the backend, and that is the order that fails. Systems amplify whatever '
         'discipline sits above them, so backend systems built under undisciplined leadership decay within a '
         'quarter. Holding the order is the intervention. There is also a real decision buried in the middle '
         'about where retention belongs, and it has consequences for at least one job description.',
 work=['We start with a measured week of where leadership time goes, rather than a recalled one',
          'Three things the leadership group tracks daily, chosen by them, plus a thirty-minute weekly '
          'reflection',
          'Your client journey becomes an operating document with every stage owned by a named person',
          'We settle where retention sits, which is a real decision rather than an implicit one',
          'One rule applied to the backend: any task done more than twice deserves a system. Your three '
          'highest-value processes documented'],
 get=['The three-pillar sheet: the whole operation on one page',
         'A leadership discipline and a scheduled weekly reflection',
         'A documented client journey with one leak fixed and the retention decision recorded',
         'The documentation backlog: every twice-done task, by function',
         'An operations manual skeleton populated with what already exists, plus three documented processes'],
 money='It is the difference between a business that grows past its founders and one that does not. The '
          'weekly reflection sounds soft, and it is the only recurring slot where anybody notices a system '
          'has stopped being used.')

u('process-capture',
 t='t4',
 type='A',
 src='molly',
 src_id='M21',
 name='Process Capture',
 time='2 weeks',
 who='Operations, enablement',
 promise='Document ten to twenty processes in two weeks by recording people doing the work instead of '
            'asking them to write it up.',
 problem='Documentation never gets written because writing it is the worst job in the building. It has '
            'been on the plan for two years. Everyone agrees it matters. Every attempt produced three '
            'excellent documents from one conscientious person and then stopped. The people who could write '
            'the best documentation have the least time, and that is no coincidence.',
 cost='Nothing can be delegated, because work that exists only as behavior cannot be handed to a new '
         'person. Nothing can be automated, because you cannot automate a process nobody wrote down. And '
         'every departure is a capability loss.',
 hard='The usual approach asks the expert to write, which costs an afternoon and therefore never happens. '
         'Invert it and the recording becomes the source of truth, with the document generated from it. That '
         'costs almost nothing, because the person is doing the work anyway. Getting people to record the '
         'messy real version rather than a tidy rehearsed one is the part that needs handling in the first '
         'twenty minutes.',
 work=['We select on three criteria including how concentrated the knowledge is in one person, which '
          'clients under-weight',
          'Twenty minutes of training on how to record: talk through the decisions, and do not tidy up first',
          'People record themselves doing their own work, roughly an hour each covering three or four '
          'processes',
          'An interview pass on what a recording cannot show: what makes it go wrong, what they check that '
          'nobody told them to, when they escalate',
          'Every checklist tested by somebody who does not normally do the task, on real work, with the '
          'owner watching and not helping'],
 get=['Ten to twenty documented processes with triggers, decisions, exceptions and owners',
         'A tested checklist for each, because a checklist gets followed and a document gets filed',
         'Verification results showing what broke when a fresh person ran it',
         'A ranked backlog of what is still undocumented',
         'The forward rule: anything done twice gets recorded, with a named owner'],
 money='It is the gate on everything automatable in your business. An agent built on an undocumented '
          "process encodes one person's habits, and nobody can tell when it drifts.",
 gate='**Capture once, reuse many times is the whole mechanism, and it works the same on a '
         'customer-facing recording as on an internal one.** Where the recording is long-form content rather '
         'than process, the conversion into clips, quotes and summaries is automated with a selection step '
         'rather than assigned to somebody, and it feeds the visibility work, since a growing library is '
         'what gets a business named.',
 absorbs=['P23 The Repurposing Engine, in part'])

u('four-real-numbers',
 t='t4',
 type='N',
 src='molly',
 src_id='M22',
 name='Four Real Numbers',
 time='1 week',
 who='CFO, COO',
 promise='Four numbers you can act on, each with a compared to what, defined in writing before anyone '
            'computes anything.',
 problem='Your dashboards are full of counts nobody can act on. Revenue, headcount, leads, tickets, '
            'sessions. All real, all moving, none of them answering whether the business is getting better '
            'at what it does. Four questions would settle most of your recurring arguments, and all four are '
            'unanswered.',
 cost='Arguments get settled by seniority instead of evidence, and the same argument comes back every '
         'quarter because nothing was resolved. You also cannot tell growth from churn-and-replace. '
         'Underpricing stays invisible, which is how a firm ends up doing its worst-margin work for its '
         'loudest customer.',
 hard='The hard part is definition, not arithmetic. What counts as a client. When do they stop being one. '
         'What counts as a lead. What spend counts as marketing spend. Each has three plausible answers, and '
         'the choice moves the number materially. The second hard part is refusing to compute a metric your '
         'data cannot honestly support. A proxy that everyone forgets is a proxy does more damage than an '
         'admitted blank.',
 work=['We settle every definition in the room and in writing before any number is produced',
          'All four computed across four quarters from source systems rather than from existing reports',
          'Where a metric cannot be produced honestly we record the blank and what would fix it, rather than '
          'substituting a proxy',
          'We separate what the trend supports from what it merely permits',
          'Three cross-reads that carry more than any single metric, including the one that reveals '
          'underpricing'],
 get=['Four metrics across four quarters, each with its formula and denominator',
         'Written, signed definitions including every judgment call made',
         'The register of blanks where data cannot support a number',
         'An owner, a cadence and a trigger threshold per metric',
         'The computation method, so your team reproduces the numbers without us'],
 money='Time spent per client against income is the metric professional services firms track least often '
          'per account. It is also the one that most often changes a pricing decision.')

u('failed-payment-recovery',
 t='t4',
 type='N',
 src='molly',
 src_id='M23',
 name='Failed Payment Recovery',
 time='1 week',
 who='CFO or finance lead, membership and subscription businesses',
 promise='Find out what you lose to failed payments each quarter, then recover most of it with a '
            'four-message sequence.',
 problem='Failed payments get handled by whoever notices. A card expires, a charge fails, a notification '
            'lands somewhere, and what happens next depends on whether anyone is looking. Finance sometimes '
            'catches it at month end, four weeks late. Ask what you lost to failed payments last quarter and '
            'the true answer is that nobody has pulled the number.',
 cost='It is revenue you already earned and are not collecting. The customer chose you, wanted to keep '
         'paying, and a card expired. Worse, involuntary churn sits inside your churn figure, which makes '
         'your churn number wrong and every churn analysis built on it wrong too.',
 hard='Nothing about the sequence is technically difficult, and two details decide whether it works. The '
         'first message has to assume a card problem rather than a decision. A collections tone converts far '
         'worse, and in the overwhelming majority of cases a card did expire. Payment retries also have to '
         'line up with the messages. A system retrying in the background while emails tell the customer to '
         'act is the most common defect, and it stays invisible until somebody maps both schedules side by '
         'side.',
 work=['We establish the number first, from four quarters of billing data, before building anything',
          'A four-message sequence on days zero, three, seven and ten, with the day-zero tone written '
          'carefully',
          'Retries aligned with messages, so the system and the emails stop contradicting each other',
          'Sensitive and enterprise accounts routed to a human instead of an automated pause',
          'A daily payment watch with a named owner, and involuntary churn separated from voluntary churn '
          'permanently'],
 get=['The leak number across four quarters, with involuntary churn split out',
         'A live four-message sequence, verified by a real card we fail deliberately',
         'Retry alignment and a tested exception route',
         'A daily watch with a named owner and a monthly leak report',
         'Post-pause design, because a paused customer is not a lost one'],
 money='This is the fastest payback on the suite. It pays for itself inside a quarter and you can see the '
          'number. We hold ourselves to that, and will say so in writing if it does not.')


# ---------------- T5 : The working relationship ----------------
u('claude-ecosystem-fork',
 t='t5',
 type='C',
 name='The Ecosystem Fork',
 time='2 days',
 who='Anyone about to commit a team to a way of working',
 promise='Which environment each person on your team should actually be in, and why it is not the same '
            'one.',
 problem='The advice in circulation is a ladder: start in chat, move to the collaborative tool, graduate '
            'to the coding environment. It was taught that way and it stopped being true within six months.',
 cost='Routing somebody up the ladder when they should go sideways costs months. A person who wants AI '
         'working with their information and processes does not need a coding environment, and putting them '
         'in one produces a confident conclusion that AI is not for them.',
 hard='Nothing technical. The difficulty is that the ladder is a more satisfying story than the fork, so '
         'it survives past the point where it describes anything.',
 work=['Classify the work each person actually does, against the three environments.',
          'Route by the shape of the work rather than by seniority or technical confidence.',
          'Name explicitly who should stop climbing, because the collaborative environment is a destination '
          'for a whole class of user rather than a waypoint.',
          'Set the assets question: where the outputs live once produced, which is the part every version of '
          'this advice omits.'],
 get=['A per-person routing, with the reasoning stated',
         'The list of people who should not move up',
         'A decision about where produced assets live',
         'A re-check trigger, since this changed inside six months once already'],
 money='Two days. It is the cheapest engagement in this tier and it decides how expensive the others are.',
 gate='**We will name people who should not be using these tools at all.** If that is not a conclusion '
         'the engagement can reach, it is not worth running.',
 src='perry',
 src_id='P8')

u('new-model-protocol',
 t='t5',
 type='C',
 name='The New-Model Release Protocol',
 time='2 days',
 who='Technical lead, whoever gets asked whether to upgrade',
 promise='A standing procedure for what happens when the model underneath you changes, so the answer is '
            'not improvisation.',
 problem='A release lands and either nothing happens or everything is torn up. Neither is a decision, and '
            'both are common.',
 cost='Launch day is the worst time to evaluate anything. Server load, usage restrictions and early '
         'rushes make the model look worse than it is, and the conclusions drawn in the first twenty-four '
         'hours persist for months.',
 hard='Believing the central claim, which sounds wrong: the model does not automatically know how to use '
         'its own improvements. Your existing instructions were written for the previous one and will '
         'quietly under-use the new one until somebody asks it to review them.',
 work=['Install the wait. Twenty-four hours, no exceptions, for the rush and the restrictions to settle.',
          'Update, set effort to the highest setting, and do not start anything from scratch.',
          'Run the re-evaluation: have the model review your existing skills, connectors, agents and prompts '
          'against its own change log, and report what it can now do better.',
          'Add the cost clause, which is what turns a capability review into a budget review in one '
          'sentence.',
          'Write the whole thing down as a standing procedure with an owner, because the value is in it '
          'firing every time.'],
 get=['The protocol, written, with an owner and a trigger',
         'The re-evaluation prompt, ready to run',
         'A first pass run against your current setup',
         'A record of what the review changed, so the next one is comparable'],
 money='Two days to install. It runs itself afterwards, which is the point.',
 gate='**This is the lightweight version.** If you are running more than a handful of skills and agents, '
         'the eight-step migration is the correct engagement and this one will under-serve you.',
 src='perry',
 src_id='P9')

u('model-migration',
 t='t5',
 type='C',
 name='The Eight-Step Model Migration',
 time='2 weeks',
 who='Technical lead on a system with real surface area',
 promise='A full migration across agents, skills, connectors and vendor files, in an order that does not '
            'overwrite your own work.',
 problem='A large setup does not migrate by updating a version number. Agents, skills, MCP connections, '
            'prompts and supporting files all encode assumptions about the model they were written against.',
 cost='The specific expensive mistake is ordering. Update your prompts first and the newer vendor files '
         'land on top of them, so the work is done twice and the second time nobody is sure what was lost.',
 hard='Step four, and it is the reason to buy this rather than improvise it: vendor files before prompts. '
         'That constraint was discovered by being burned, not derived, and it is not obvious in either '
         'direction until it has cost you.',
 work=['Give the agent the current documentation for the new model, rather than describing it.',
          'Create the model-selection framework first, so routing exists before anything is rewritten.',
          'Audit the estate: agents, skills, MCP connections, prompts, supporting files, with counts.',
          'Update vendor files, then rewrite prompts. Never the other way.',
          'Add the recurring checks, test against a real task rather than a self-report, correct the model '
          'when it claims success it has not verified, then run the final prompting sweep.'],
 get=['The migrated estate, with a before-and-after inventory',
         'A model-selection framework, written',
         'Scheduled re-checks with owners',
         'A real-task test result, not a self-report'],
 money='Two weeks for a system of any size. The source ran it against more than a hundred skills.',
 gate='**Step seven includes a standing rule we will install whether you ask or not:** the agent may not '
         'claim something is complete unless it has verified the result. If that rule is unwelcome, this is '
         'the wrong supplier.',
 src='perry',
 src_id='P10')

u('preparation-before-prompts',
 t='t5',
 type='C',
 name='Preparation Before Prompts',
 time='1 week',
 who='Anyone whose AI work keeps failing in ways nobody can reproduce',
 promise='The four things that have to exist before a prompt is worth writing, installed.',
 problem='Complex work gets handed to a model cold, with a well-crafted instruction and nothing else. It '
            'half-works, unpredictably, and the response is to improve the prompt.',
 cost='Prompt refinement against a preparation problem is the most expensive loop in this whole field, '
         'because it is nearly free to stay in. Teams spend quarters improving instructions against a '
         'ceiling instructions cannot move.',
 hard='Accepting that the prompt is the last step rather than the first. Everything upstream of it is '
         'unglamorous: a dedicated skill, research into the target system, guardrails, and enough context '
         'for the model to make a judgement rather than a guess.',
 work=['Create the dedicated skill for the task, rather than describing the task in a prompt.',
          'Research the target platform and put what you find where the model can read it.',
          'Add the guardrails: what it must not do, and what it must confirm before proceeding.',
          'Supply the context needed to decide, not just to execute.',
          'Install the improvement loop, because a skill that never changes after a successful run is '
          'wasting the run.'],
 get=['A working skill for your highest-value repeated task',
         'The guardrail set, written',
         'A context pack the model actually reads',
         'The improvement loop, with a trigger'],
 money='One week. It is the engagement most likely to make an existing failing setup start working '
          'without replacing anything.',
 gate='**We will tell you where the prompt stops mattering.** For agentic work with tools and a browser, '
         'the practitioner this comes from says plainly there was no secret sauce in his prompt, and we are '
         'not going to sell you prompt craft into that case.',
 src='perry',
 src_id='P11')

u('instructions-interview',
 t='t5',
 type='C',
 name='The Global-Instructions Interview',
 time='2 days',
 who='Every individual using the tool, one at a time',
 promise='A complete instruction file per person, produced by interview rather than by template.',
 problem='Global instructions get written once, from a blank page, by somebody guessing at what matters. '
            'They are generic, and being generic is the one thing they cannot afford to be.',
 cost='A weak instruction file is not neutral. It is re-read at the start of every session, so every '
         'vague line is a small tax paid thousands of times, and nobody attributes the resulting friction to '
         'it.',
 hard='Nothing, once you know the move. Hand the model the questions and make it ask them one at a time, '
         'waiting for each answer, then write the file. The version where somebody answers all five at once '
         'produces a visibly worse file.',
 work=['Run the five-question interview per person: role and what they do, how they want to be spoken to '
          'and which behaviours annoy them, three things never to do, three non-negotiable safety rules, '
          'spelling and always-on context.',
          'Have the model write the complete file in one block, then review it against what was actually '
          'said.',
          'Extend it for the heavier users with the thirty-question version, which loops until the model '
          'states it is clear.',
          'Install it, and set a review trigger.'],
 get=['A complete instruction file per person',
         'The interview transcript, so the file can be re-derived',
         'The thirty-question extension for heavy users',
         'A review trigger'],
 money='Two days for a team. It is the highest ratio of benefit to effort anywhere on this site.',
 gate='**It has to be one question at a time.** If the process gets compressed to save an afternoon, the '
         'output is a template and you should not pay us for a template.',
 src='perry',
 src_id='P12')

u('memory-persistence',
 t='t5',
 type='C',
 name='Memory and Context Persistence',
 time='2 days',
 who='Anyone who has re-explained their project to a model more than twice',
 promise='A memory file the model reads first, every session, without being asked.',
 problem='The single most common complaint in eighteen months of live sessions is losing context between '
            'conversations. People re-explain the same project weekly.',
 cost='Re-establishing context is not just the time it takes. The model works from whatever the person '
         'remembered to mention this time, so the quality of the work varies with the quality of the '
         're-explanation, and nobody can see that happening.',
 hard='The initiation, not the file. Writing a memory file is easy. Making it the first thing read on '
         'every new conversation is the part people skip, and without it the file is a document nobody '
         'opens.',
 work=['Create the memory file and decide what belongs in it, which is state rather than instruction.',
          'Wire the project instruction file to check it at the start of every conversation.',
          'Set the update discipline: what gets written back, when, and by whom.',
          'Test across a session boundary, with a real task, rather than asking the model whether it '
          'worked.'],
 get=['The memory file, populated',
         'The initiation wiring, tested across a session boundary',
         'A write-back discipline',
         'A convention that survives more than one project'],
 money='Two days. Pairs with the instructions interview and we would rather do both at once.',
 gate='**Memory is state, not instructions.** If what you actually need is for the model to behave '
         'differently, that is the interview engagement above and this one will not fix it.',
 src='perry',
 src_id='P13')


# ---------------- T6 : AI systems and agent build ----------------
u('build-your-brain',
 t='t6',
 type='C',
 src='molly',
 src_id='M25',
 name='Build Your Brain Program',
 time='2 weeks',
 who='Any function, enablement',
 promise='Train six to twelve of your people to build their own AI assistants on their own real work, and '
            'to fix them when they go wrong.',
 problem='People paste the same context into a chat window forty times a week. Everyone has access. Every '
            'session starts from zero. A few people built something better, and it lives in their personal '
            'accounts where nobody else can find it. When someone builds one for the team, it demos well and '
            'produces wrong-shaped output in real use, and the effort gets abandoned instead of diagnosed.',
 cost='The same context gets re-explained thousands of times a year, a small tax paid continuously by '
         'everyone. And quality varies by who is prompting, with no mechanism to level it up because the '
         'skill is undocumented.',
 hard='Attempts fail for one of exactly two reasons, and teams cannot tell which. So they tinker for a '
         'week and give up. There is a diagnostic that separates the two cleanly, and once a team has it '
         'they fix their own builds in an afternoon. Getting there takes real use between sessions rather '
         'than a single training day. The log of what went wrong is the teaching material.',
 work=['Each participant brings a real weekly task, tested against three questions before anything is '
          'built',
          'An archetype chosen before a word is written, which is where half the vagueness gets removed',
          'A five-part build standard, with the diagnostic taught explicitly so the framework becomes '
          'self-correcting',
          'Three days of real use, with each participant logging what came back wrong-shaped and what came '
          'back generic',
          'A full day diagnosing and repairing their own builds in the room, seeing the change take effect '
          'immediately',
          'Where an assistant answers customers by voice or chat, the deployment decisions are made '
          'deliberately: what sits in the prompt for speed, what sits in the knowledge base, consolidated to '
          'one document, and booking enabled as a named action rather than asked for in the prompt'],
 get=['Three to five live assistants, built by your people on real work',
         'The build standard, the archetype picker and the diagnostic rule',
         'Required constraints as reusable text, including house style written as incapacity rather than '
         'prohibition',
         'An assistant register giving every one an owner, a purpose and a review date',
         'Use logs showing what each participant found and changed',
         'For customer-facing assistants, the deployment decisions written down: prompt versus knowledge '
         'base, and the named actions enabled'],
 money='A built assistant is one assistant. A trained cohort is a capability, and it is why we teach '
          'rather than build. The register is what stops you accumulating forty assistants of unknown '
          'provenance within a year.',
 gate='**The failure repeated across the source material is a generic-sounding agent that never books '
         'anything.** In every diagnosed case the prompt was the default and booking had never been enabled. '
         'For customer-facing deployments we hand over after a testing period and do not monitor '
         'indefinitely.',
 absorbs=['P18 Voice and Chat Agent Deployment, in part'])

u('ai-agent-roster',
 t='t6',
 type='C',
 src='molly',
 src_id='M26',
 name='AI Agent Roster',
 time='4 weeks',
 who='COO, CTO',
 promise='Give your automations an org chart. One named human owner per agent. Nothing reaches a customer '
            'without a person in the path.',
 problem='You have a dozen disconnected automations and nobody owns them. Different people built them at '
            'different times for good reasons. Some are excellent. Nobody has a list. When one produces '
            'something wrong, finding the responsible person takes a day, and the answer is usually someone '
            'who moved teams. Each automation is fine on its own. What is missing is the structure every '
            'other part of the company already has.',
 cost='Errors get found by customers rather than by you, because an unreviewed automated output is a '
         'system publishing on your behalf with no editor. Nothing improves because nothing is owned. And '
         'you cannot answer the governance question when somebody finally asks it.',
 hard='The temptation is to build more agents. What fails is the absence of structure around them. '
         'Building the review gate before the agent sounds backwards, and it prevents the most common '
         'failure: a gate added later and never. Refusing to build agents on undocumented processes is the '
         'other unpopular position. It is the one that most reliably separates a working roster from an '
         'expensive one.',
 work=['We inventory everything already running, which routinely surfaces automations nobody knew about',
          'We design a roster of standing roles rather than a list of tools, with explicit '
          'non-responsibilities',
          'One named human owner per agent, agreed out loud in the room, with what ownership means written '
          'down',
          'Schedule times deliberately offset by a minute or two, which buys rate limiting and readable logs '
          'for free',
          'Three to five agents built inside the structure, only for processes that have been documented',
          'Where agents work under an orchestrator, each specialist gets one job, only the context that job '
          'needs, and a scope fence written into it: you are not doing other work, this is the only thing '
          'you do. Without the fence the specialists drift back into one generalist within weeks and nobody '
          'notices'],
 get=['The automation inventory, including what nobody knew was running',
         'An agent roster with roles, owners and non-responsibilities',
         'A scheduled-task calendar and a risk-marked register',
         'Review gates per agent, demonstrated',
         'An operating document written from the week your team ran it, including the failures',
         'A context boundary and a scope fence per agent, with its activation condition written'],
 money='It is the difference between a dozen automations you tolerate and a system you can extend, staff '
          'and answer for. We will not build agents that publish or transact without a human in the path, '
          'and we will tell you why.',
 gate='**The shape is portable and the members are not.** Two independent rosters exist in the source '
         'material, one organised by software discipline and one by marketing deliverable. Every member '
         'changes and the orchestrator-plus-specialists shape does not, which is what proves it is '
         'architecture rather than habit. Autonomous-agent patterns can also get an account suspended, so we '
         "design inside the vendor's terms and say where that limits what you wanted.",
 absorbs=['P14 The Specialised-Subagent Install'])

u('company-brain',
 t='t6',
 type='C',
 src='molly',
 src_id='M27',
 name='Company Brain',
 time='3 weeks',
 who='Chief of staff, operations',
 promise='A company knowledge base that gets more accurate over time, with a check that hunts down its '
            'own stale facts.',
 problem='What the company knows dies with whoever holds it, and your AI tools re-learn the company every '
            'session. Both are the same problem. Company knowledge lives in heads, old decks, a wiki nobody '
            'updates, and four thousand documents nobody can search. The wiki failed for the same reason the '
            'documentation failed.',
 cost='Senior people spend hours a week being a lookup service. Departures are capability losses. And '
         "stale knowledge is actively harmful, because a wiki with last year's pricing is worse than no "
         'wiki: somebody will act on it.',
 hard='Every knowledge base decays, and the decay is gradual enough that nobody notices the moment it '
         'stopped being trustworthy. The part that rarely gets built is a staleness detector, hunting '
         'contradictions like old pricing against new, or programs described as current after they ended. '
         'The other discipline is scope. The instinct is to migrate everything, and everything is unusable.',
 work=['Source vetting before anything is ingested: name the sources by name, official documentation, '
          'change logs, the individuals whose work you actually trust, and write the exclusion rule down, '
          'because information from an invalid source is feeding the thing you will later rely on',
          'We push hard on scope on day one, using one test: would somebody, or an assistant, need this to '
          'answer a question about the company',
          'Six foundation files built in a deliberate order: facts, identity, voice, audience, offers, '
          'market',
          'Ingest that integrates rather than summarizes, updating every existing page a new source touches',
          'Query that answers across pages with citations and saves substantial answers back',
          'A lint operation built and run live on your own vault, with the first contradictions resolved '
          'together',
          'Connect the vault to your agent environment, so agents read from it rather than from whatever was '
          'to hand',
          'A written recovery procedure, because these structures get away from people. The fix is asking '
          'the system to reorganise itself and walk you through it'],
 get=['Six foundation files and a structured, indexed vault',
         'Ingest, query and lint running',
         'Four scheduled routines including a ten-minute weekly update',
         'Conventions enforced rather than encouraged, with a check',
         'Named owners for the lint cadence and the weekly update, plus the out-of-cycle triggers',
         'A named source list with the reason each one is on it, and a written exclusion rule',
         'The vault connected to your agent environment'],
 money='Knowledge compounds instead of being re-derived every session, and every AI tool you point at the '
          'company stops starting cold. The lint cadence is what keeps that true in month nine.',
 gate='**This is the engagement clients most often want without the vetting, and we decline that '
         'combination.** A knowledge base built from whatever was to hand is worse than none, because it is '
         'trusted, and once a bad source is inside, its claims come back as answers nobody can trace. The '
         'weekly update is a scheduled job with an owner, not an intention.',
 absorbs=['P7 Source Vetting for a Knowledge Base', 'P16 The Second Brain Build'])

u('skill-authoring',
 t='t6',
 type='C',
 name='Skill Authoring and the Improvement Loop',
 time='2 weeks',
 who='Whoever will own the skills after we leave',
 promise='Skills as the shipped unit, with a loop that makes each successful run improve the next one.',
 problem='Capability lives in prompts people keep in documents, in their heads, or in a chat history. It '
            'cannot be versioned, handed over, or improved deliberately.',
 cost='Undocumented capability leaves with the person. More quietly, a skill that never changes after a '
         'successful run throws away the only free information you get, which is what worked.',
 hard='The loop, not the authoring. Writing a skill file is straightforward. Establishing that every '
         'successful run is an opportunity to improve the next one requires a trigger and an owner, or it '
         'does not happen.',
 work=['Identify the repeated work worth turning into skills, in order of frequency.',
          'Author each as a skill file with its activation condition, scope and tools.',
          'Install the improvement loop with an explicit trigger, on the stated principle that skills should '
          'never remain static.',
          'Set the review cadence against vendor changes, since skills written for one model under-use the '
          'next.',
          'Hand over with a standard, so the next skill somebody writes looks like these.'],
 get=['A skill set for your highest-frequency work',
         'An authoring standard the team can follow',
         'The improvement loop, with a trigger and an owner',
         'A review cadence tied to vendor releases'],
 money='Two weeks. This is the engagement that determines whether anything else in this tier survives our '
          'leaving.',
 gate='**We will not author skills for work you have not yet done manually.** A skill written before the '
         'task is understood encodes a guess, permanently.',
 src='perry',
 src_id='P15')

u('browser-automation',
 t='t6',
 type='C',
 name='Browser Automation Install',
 time='2 weeks',
 who='Ops lead, whoever owns a platform with no usable API',
 promise='An agent that drives a logged-in browser through work that has no API, built as a reusable '
            'skill.',
 problem='The most repetitive work in a marketing operation sits inside vendor interfaces that expose no '
            'automation. People do it by hand because there is no other option.',
 cost='Hand-operated platform work is the largest recoverable cost in most small operations and the least '
         "visible, because it is spread across everybody's week in half-hour pieces.",
 hard='Not the prompt. The practitioner this comes from, asked what he typed, said there was no secret '
         'sauce in his prompt. The difficulty is preparation and guardrails: what the agent may touch, what '
         'it must confirm, and what happens when the interface moves.',
 work=['Pick the target workflow by frequency and by how mechanical it is.',
          'Create the skill and let the agent research the target platform before it touches anything.',
          'Set the guardrails: which account, which actions, what requires confirmation, what is never '
          'permitted.',
          'Run it live against real work with somebody watching, then iterate. Delays and troubleshooting '
          'are the normal shape of this, not a sign it is failing.',
          'Alternatively record the workflow being done by hand and convert the recording into the skill, '
          'which is now the faster route for well-defined tasks.'],
 get=['A working browser skill for one real workflow',
         'A guardrail set, written',
         'A live supervised run',
         'The pattern documented so the second workflow is cheaper'],
 money='Two weeks for the first workflow. The second and third are substantially less.',
 gate='**Interfaces move and this breaks when they do.** We will say which parts are brittle and build '
         'the check that tells you it broke, rather than letting you find out from a customer.',
 src='perry',
 src_id='P17')

u('port-architecture',
 t='t6',
 type='C',
 name='Prototype and Port Architecture',
 time='3 weeks',
 who='Technical lead running agents at cost',
 promise='Agents modelled where iteration is cheap, then ported to where running them is cheap, with '
            'security and token cost as the constraints.',
 problem='Agents get built where they will run, so every iteration costs production money, and the first '
            'architecture is the one you are stuck with.',
 cost='Building in the expensive environment makes experimentation expensive, so less of it happens, so '
         'the design is worse. The cost shows up as a bill and the real loss is the iterations nobody ran.',
 hard='The porting constraints, in order. Security first, token management first, and only then '
         'equivalence of output. Most ports are attempted in the reverse order and get abandoned when the '
         'bill or the exposure surfaces.',
 work=['Model the agent where iteration is cheapest and confirm it does what you want.',
          'Port with security as the leading constraint, deciding what the runtime may reach.',
          'Then token management: what runs on subscription capacity, what runs on a local model, and where '
          'quality genuinely requires the expensive route.',
          'Verify equivalence on real tasks rather than on a self-report.',
          'Document both halves, because the prototype is now the specification.'],
 get=['The agent running in the target runtime',
         'A security boundary, written',
         'A token-cost comparison across routes',
         'An equivalence test on real tasks'],
 money='Three weeks. Worth it where the agent runs often; not worth it where it runs weekly.',
 gate='**We will name where a cheaper local model does not hold quality.** The source assumes it can and '
         'offers no measurement, and we are not going to inherit that assumption on your behalf.',
 src='perry',
 src_id='P19')

u('vibe-coded-build',
 t='t6',
 type='C',
 name='Vibe-Coded Application Build',
 time='2 weeks',
 who='Founder with a tool-shaped idea and no development team',
 promise='A working internal tool or client-facing app, specified properly and built where the credits go '
            'furthest.',
 problem='The build platforms are good enough now that the constraint is the specification, not the '
            'coding. Most attempts fail at the brief.',
 cost='Building straight into the most expensive platform from a vague description is how a fortnight of '
         'credits becomes a prototype nobody wants. The first build is what costs, and it costs most when '
         'the spec was thin.',
 hard='The spec, and the platform choice. The technique the source arrives at is to have one model '
         'produce a complete, structured specification, then hand that to the build platform. Choosing the '
         'platform on cost rather than on reputation is the second half.',
 work=['Turn the idea into a structured specification: objective, users, screens, data, constraints, and '
          'what done means.',
          'Choose the build environment on cost and output quality for your case rather than by default.',
          'Build the first working version, then move it to a hosting environment if the build tool is not '
          'where it should live.',
          'Handle domain, payments and access properly, which is where most of these stall.',
          'Hand over with the specification, since that is the durable artifact.'],
 get=['A working application',
         'The specification, which outlives the platform',
         'Domain, hosting and access configured',
         'A cost comparison for the next build'],
 money='Two weeks for a first version. Ambition is the variable, not the timeline.',
 gate='**We will tell you when the answer is an existing product.** A meaningful share of what people '
         'want built here already exists inside a subscription they hold.',
 src='perry',
 src_id='P20')

