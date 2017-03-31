#!/usr/bin/env python3

# This module will contain a software model of the the FPGA for viewing

class Page:
    virtAddr = None # Address in virtual memory
    data = [] # Data within memory

    # Constructor
    def __init__(self, page_size, p_virtAddr):
        self.data = [0 for x in range(page_size)]
        self.virtAddr = p_virtAddr

class Model:
    virtualMem = [] # Contains full list of pages, held in virutal memory
    physicalMem = [] # Contains list of pages in physical memory
    curAddr = None # Current address of FPGA
    pagetable = [] # Copy of page table
    # Update variables
    reqVAddr = None
    pageResult = None
    reqVOff = None
    valid = None
    reqPhAddr = None
    pageOut = None
    pageIn = None
    fifo = []

    # Constructor
    def __init__(self, num_pages, num_frames, page_size):
        self.virtualMem = [Page(page_size,(x*page_size)) for x in range(num_pages)]
        self.physicalMem = [0 for x in range(num_frames)]
        self.pagetable = [(0,False) for x in range(num_pages)]

    # Load page from virtual memory to physical memory
    def _pagein(self, pagenum, framenum):
        # Place page into physical memory
        self.physicalMem[framenum] = self.virtualMem[pagenum]
        # Update page table
        self.pagetable[pagenum] = (framenum,True)
        # Update variables
        self.pageIn = pagenum

    # Remove page from physical memory
    def _pageout(self, pagenum, framenum):
        # Remove page from physical memory
        self.physicalMem[framenum] = 0
        # Update page table
        self.pagetable[pagenum] = (0,False)

    # Parse input
    def parsein(self, msg):
        # TODO Determine messages, create parsing techniques for messages
        return 0
